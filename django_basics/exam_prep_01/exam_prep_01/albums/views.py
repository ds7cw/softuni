from django.shortcuts import render
from exam_prep_01.albums.models import Album


# Create your views here.
def album_add(request):
    
    return render(request, 'album-add.html')


def album_details(request, id):

    album = Album.objects.get(id=id)
    context = {'album': album}

    return render(request, 'album-details.html', context)


def album_edit(request, id):

    return render(request, 'album-edit.html')


def album_delete(request, id):

    return render(request, 'album-delete.html')