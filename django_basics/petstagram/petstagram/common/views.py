from django.shortcuts import redirect, render
from petstagram.photos.models import Photo
from .models import PhotoLike


# Create your views here.
def home_page(request):
    all_photos = Photo.objects.all()

    context = {'all_photos': all_photos}
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    liked_obj = PhotoLike.objects.filter(to_photo=photo_id).first()

    if liked_obj:
        liked_obj.delete()
    else:
        like = PhotoLike(to_photo=photo)
        like.save()
    
    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')