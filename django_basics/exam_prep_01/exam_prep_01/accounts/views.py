from django.shortcuts import render, redirect
from exam_prep_01.accounts.models import Profile
from exam_prep_01.albums.models import Album
from exam_prep_01.accounts.forms import ProfileModelForm

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    form = ProfileModelForm()
    context = {
        'profile': profile,
        'add_profile_form': form,
    }

    if profile:
        albums = Album.objects.filter(owner=profile)
        context['albums'] = albums
        return render(request, 'home-with-profile.html', context)
    
    elif request.method == 'POST':
        
        """
            print(request.POST)
            <QueryDict: {
                'csrfmiddlewaretoken': [
                    'a8Afeih5Xugf6LvE1HKHpuRt4heX5isKCunvMssKbF6Y1GUEaXx4Q4QBp6fSw3sI'], 
                    'username': ['ddd'], 'email': ['ddd@ddd.com'], 'age': ['22']
                }>
            [07/Feb/2024 11:22:23] "POST / HTTP/1.1" 200 2339

            username = request.POST['username']
            email = request.POST['email']
            age = request.POST['age']
            print('{} {} {}'.format(username, email, age))
        """
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    albums_count = Album.objects.filter(owner=profile).count()
    context = {'profile': profile, 'albums_count': albums_count}

    return render(request, 'profile-details.html', context=context)


def profile_delete(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    
    if request.method == 'POST':
        if profile:
            profile.delete()
            return redirect('home')

    return render(request, 'profile-delete.html', context=context)
