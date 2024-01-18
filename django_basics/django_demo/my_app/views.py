from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email_addres = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            my_user = User.objects.create_user(username=username, email=email_addres, password=pass1)
            my_user.last_name = lname
            my_user.first_name = fname
            my_user.save()

            messages.success(request, 'Account has been successfully created!')
            return redirect('signin')
    else:
        return render(request, 'authentication/signup.html')


def signin(request):
    return render(request, 'authentication/signin.html')


def signout(request):

    return redirect('home')
