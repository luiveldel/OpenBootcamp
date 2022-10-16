import uuid

from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del genero")

    def __str__(self):
        """Representacion informal de un objeto"""
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text="Sinopsis de la pelicula")
    genre = models.ManyToManyField(Genre) # Una pelicula tiene varios generos asociados

    def __str__(self):
        """Cuando se invoque a las peliculas se referenciara por su titulo"""
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])

class FilmInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico")
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad de la pelicula')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.film.title)

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)