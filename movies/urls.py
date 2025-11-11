# movies/urls.py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/create/', views.movie_create, name='movie_create'),
    path('movie/<int:movie_id>/edit/', views.movie_edit, name='movie_edit'),
    path('movie/<int:movie_id>/delete/', views.movie_delete, name='movie_delete'),
]