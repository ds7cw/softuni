from django.urls import path, include
from exam_prep_01.albums import views

urlpatterns = [
    path('add/', views.album_add, name='album-add'),
    path('<int:id>/', include(
        [
            path('details/', views.album_details, name='album-details'),
            path('edit/', views.album_edit, name='album-edit'),
            path('delete/', views.album_delete, name='album-delete'),
        ]
    )),
    
]
