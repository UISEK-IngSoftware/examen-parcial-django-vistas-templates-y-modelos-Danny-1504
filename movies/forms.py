from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'director', 'publication_year', 'synopsis']
        widgets = {
            'synopsis': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ingresa la sinopsis de la película...'}),
            'publication_year': forms.NumberInput(attrs={'min': 1900, 'max': 2030}),
            'title': forms.TextInput(attrs={'placeholder': 'Título de la película'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Ej: Acción, Drama, Comedia'}),
            'director': forms.TextInput(attrs={'placeholder': 'Nombre del director'}),
        }
        labels = {
            'title': 'Título de la Película',
            'genre': 'Género',
            'director': 'Director',
            'publication_year': 'Año de Publicación',
            'synopsis': 'Sinopsis',
        }