from django.shortcuts import redirect, render
from petstagram.photos.models import Photo
from .models import PhotoLike


# Create your views here.
def home_page(request):
    pet_name_pattern = request.GET.get('pet_name_pattern', None)
    all_photos = Photo.objects.all()
    print(pet_name_pattern)

    if pet_name_pattern:
        all_photos = all_photos.filter(tagged_pets__name__icontains=pet_name_pattern)

    context = {'all_photos': all_photos, 'pet_name_pattern': pet_name_pattern}
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