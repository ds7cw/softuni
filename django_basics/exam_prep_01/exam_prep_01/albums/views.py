from django.shortcuts import render, redirect
from exam_prep_01.albums.models import Album
from .forms import AlbumModelForm
from exam_prep_01.accounts.models import Profile


# Create your views here.
def album_add(request):
    
    profile = Profile.objects.first()
    form = AlbumModelForm()
    context = {'add_album_form': form, 'profile': profile}
    
    if not profile:
        return redirect('home')
    
    if request.method == 'POST':
        """
            print(request.POST)
            <QueryDict: {
                'album_name': ['asd'], 'artist': ['dsa'],
                'genre': ['Jazz Music'], 'description': ['some amazing jazz album'],
                'image_url': ['http://test.com/album/add/'], 'price': ['2.99']
            }>   
        """
        
        form = AlbumModelForm(request.POST)
        
        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.owner = profile
            new_album.save()
            return redirect('home')

    return render(request, 'album-add.html', context=context)


def album_details(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    context = {'album': album, 'profile': profile}

    return render(request, 'album-details.html', context)


def album_edit(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    form = AlbumModelForm(instance=album)
    context = {'album': album, 'edit_album_form': form, 'profile': profile}

    if request.method == 'POST':
        form = AlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()

            return redirect('album-details', id=album.id)

    return render(request, 'album-edit.html', context=context)


def album_delete(request, id):

    return render(request, 'album-delete.html')