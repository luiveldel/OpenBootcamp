from django.shortcuts import render

from .models import Film, Director, FilmInstance, Genre

def index(request):
    num_film = Film.objects.all().count()
    num_instances = FilmInstance.objects.all().count()
    num_director = Director.objects.all().count()
    num_genre = Genre.objects.all().count()

    disponibles = BookInstance.objects.filter(status__exact='a').count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_film,
            'num_authors': num_director,
            'disponibles': disponibles,
            'num_instances': num_instances,
            'num_genre': num_genre
        }
    )
