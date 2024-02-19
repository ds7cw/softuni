from django.contrib import admin
from .models import PhotoComment


# Register your models here.
@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    pass
