from django.contrib import admin
from petstagram.photos.models import Photo

# Register your models here.
@admin.register(Photo)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'location', 'date_of_publication', 'short_description', 'get_tagged_pets']

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join(p.name for p in obj.tagged_pets.all())
    
    def short_description(self, obj):
        return obj.description[:15] + '...'