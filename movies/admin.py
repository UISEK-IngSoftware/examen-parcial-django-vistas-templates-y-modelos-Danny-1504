from django.contrib import admin

from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director', 'publication_year')
    list_filter = ('genre', 'publication_year')
    search_fields = ('title', 'director')
    fieldsets = (
        ('Información Principal', {
            'fields': ('title', 'genre', 'director', 'publication_year')
        }),
        ('Contenido', {
            'fields': ('synopsis',)
        }),
    )
