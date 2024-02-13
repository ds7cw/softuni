from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Player
from .forms import PlayerModelForm, DeletePlayerModelForm
from django.views.generic.base import TemplateView


# Create your views here.
def home(request):
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'main/home.html', context)


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email_addres = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'This username already exists!')
            return redirect('home')
        
        if len(username) < 3:
            messages.error(request, 'Username must be at least 3 characters long!')
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, 'Username must contain only Alpha-Numeric characters!')
            return redirect('home')

        if User.objects.filter(email=email_addres):
            messages.error(request, 'This email is already registered!')
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, 'The password and confirm password do not match!')
            return redirect('home')

        my_user = User.objects.create_user(username=username, email=email_addres, password=pass1)
        my_user.last_name = lname
        my_user.first_name = fname
        my_user.save()

        messages.success(request, 'Account has been successfully created!')
        return redirect('signin')
    else:
        return render(request, 'authentication/signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, 'main/home.html')
        
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('signin')

    return render(request, 'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


def player_create(request):
    form = PlayerModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = PlayerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'players/player-create.html', context) 


def player_details(request, pk):
    player = Player.objects.get(pk=pk)
    context = {'player': player}
    return render(request, 'players/player-details.html', context)


def player_edit(request, pk):
    player = Player.objects.get(pk=pk)
    form = PlayerModelForm(instance=player)
    
    if request.method == 'POST':
        form = PlayerModelForm(request.POST, instance=player)
        
        if form.is_valid():
            form.save()

            return redirect('player-details', pk=player.id)
    
    context = {'player': player, 'form': form}
    return render(request, 'players/player-edit.html', context)


def player_delete(request, pk):
    player = Player.objects.get(pk=pk)
    form = DeletePlayerModelForm(instance=player)
    
    if request.method == 'POST':
            print(request.POST)
            print(player)
            player.delete()
            return redirect('home')
    
    context = {'player': player, 'form': form}
    return render(request, 'players/player-delete.html', context)


class PlayersTableView(TemplateView):

    template_name = 'players/player-table.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.all()
        return context