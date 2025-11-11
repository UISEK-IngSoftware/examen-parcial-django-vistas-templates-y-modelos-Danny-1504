# movies/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Película agregada exitosamente!')
            return redirect('movies:movie_list')
    else:
        form = MovieForm()
    
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Agregar Película'})

def movie_edit(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Película actualizada exitosamente!')
            return redirect('movies:movie_list')
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Editar Película', 'movie': movie})

def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        movie.delete()
        messages.success(request, '¡Película eliminada exitosamente!')
        return redirect('movies:movie_list')
    
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})