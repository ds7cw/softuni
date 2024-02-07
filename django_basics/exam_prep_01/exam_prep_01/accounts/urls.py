from django.urls import path, include
from exam_prep_01.accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', include(
        [
            path('details/', views.profile_details, name='profile-details'),
            path('delete/', views.profile_delete, name='profile-delete'),
        ]
    )),
]
