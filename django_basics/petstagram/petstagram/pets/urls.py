from django.urls import path, include
from petstagram.pets import views

urlpatterns = [
    path('create/', views.pet_create, name='create-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details, name='details-pet'),
        path('edit/', views.pet_edit, name='edit-pet'),
        path('delete/', views.pet_delete, name='delete-pet')
    ]))
        
]