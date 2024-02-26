from django.urls import path, include
from petstagram.pets import views

urlpatterns = [
    path('create/', views.PetCreateView.as_view(), name='create-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailView.as_view(), name='details-pet'),
        path('edit/', views.PetEditView.as_view(), name='edit-pet'),
        path('delete/', views.pet_delete, name='delete-pet')
    ]))
        
]