from django.contrib import admin

from .models import Director, Genre, Film, FilmInstance

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(FilmInstance)
