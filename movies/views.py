# movies/views.py
from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list(request):
    """Vista para mostrar el listado de películas"""
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    """Vista para mostrar los detalles de una película específica"""
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})