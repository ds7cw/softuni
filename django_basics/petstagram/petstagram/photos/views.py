from django.shortcuts import render, redirect
from .models import Photo
from petstagram.common.models import PhotoComment


# Create your views here.
def add_photo(request):
    context = {}

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    pet_photo = Photo.objects.get(pk=pk)
    context = {
        'pet_photo': pet_photo,
    }

    if request.method == 'POST':
        comment_body = request.POST.get('comment_body')
        
        new_comment = PhotoComment(text=comment_body, to_photo=pet_photo)
        new_comment.save()
        return redirect('details-photo', pk=pet_photo.pk,)

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    context = {}
    
    return render(request, 'photos/photo-edit-page.html', context)

