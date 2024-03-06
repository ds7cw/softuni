from django.urls import path, include
from .views import index_page

urlpatterns = [
    path('', index_page, name='index-page'),
]