from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import generic
from petstagram.photos.models import Photo
from .models import PhotoLike


# Create your views here.
# def home_page(request):
#     pet_name_pattern = request.GET.get('pet_name_pattern', None)
#     all_photos = Photo.objects.all()
#     # print(pet_name_pattern)

#     if pet_name_pattern:
#         all_photos = all_photos.filter(tagged_pets__name__icontains=pet_name_pattern)

#     context = {'all_photos': all_photos, 'pet_name_pattern': pet_name_pattern}
#     return render(request, 'common/home-page.html', context)


class HomeView(generic.ListView):

    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related('photolike_set')
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_name_pattern'] = self.pet_name_pattern or ''
        return context

    @property
    def pet_name_pattern(self):
        return self.request.GET.get("pet_name_pattern", None)
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        queryset = self.filter_by_pet_name_pattern(queryset)
        
        return queryset
    
    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        if pet_name_pattern:
            self.request.session['pet_name_pattern'] = pet_name_pattern
        else:
            self.request.session.pop('pet_name_pattern', None)

        pet_name_session = self.request.session.get('pet_name_pattern')

        filter_query = {}

        if pet_name_pattern:
            # filter_query['tagged_pets__name__icontains'] = pet_name_pattern
            filter_query['tagged_pets__name__icontains'] = pet_name_session
        return queryset.filter(**filter_query)
 

def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    liked_obj = PhotoLike.objects.filter(to_photo=photo_id).first()

    if liked_obj:
        liked_obj.delete()
    else:
        like = PhotoLike(to_photo=photo)
        like.save()
    
    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')