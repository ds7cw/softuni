from django.urls import path, include
from petstagram.common.views import home_page, like_functionality

urlpatterns = [
    path('', home_page, name='home-page'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
]