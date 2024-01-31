from django.urls import path, include
from petstagram.accounts import views

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('signin/', views.signin_user, name='signin'),
    path('signout/', views.signout_user, name='signout'),
    path('profile/<int:pk>/', include([
        path('', views.details_user, name='profile-details'),
        path('edit/', views.edit_user, name='profile-edit'),
        path('delete/', views.delete_user, name='profile-delete'),
    ])),
]