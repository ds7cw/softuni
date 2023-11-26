from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'common/index.html')


def create_album(request):
    return render(request, 'albums/create-album.html')


def details_album(request, id):
    return render(request, 'albums/album-details.html')


def edit_album(request, id):
    return render(request, 'albums/edit-album.html')


def delete_album(request, id):
    return render(request, 'albums/delete-album.html')


def create_song(request):
    return render(request, 'songs/create-song.html')