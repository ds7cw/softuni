from django.urls import path, include
from petstagram.common.views import like_functionality, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
]