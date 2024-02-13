from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('player/', include(
        [
            path('create/', views.player_create, name='player-create'),
            path('<int:pk>/details/', views.player_details, name='player-details'),
            path('<int:pk>/edit/', views.player_edit, name='player-edit'),
            path('<int:pk>/delete/', views.player_delete, name='player-delete'),
            path('table/', views.PlayersTableView.as_view(), name='player-table'),
        ]
    )),
]