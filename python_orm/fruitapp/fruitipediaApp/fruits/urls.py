from django.urls import path, include
from fruits import views


urlpatterns = (
    path('', views.index, name='index'),
)