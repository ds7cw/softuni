from django.urls import path, include
from .views import create_pc

urlpatterns = [
    path('create-pc/', create_pc, name='create-pc')
]