from django.db import models
from django.utils import timezone



class Colección(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    fecha_de_publicacion = models.DateField(blank=True, null=True)
    editorial = models.CharField(max_length=100, blank=True, null=True)
    resumen = models.TextField(max_length=1000, blank=True, null=True) 
    GENERO_CHOICES = (
    ('Ciencia Ficción', 'Ciencia Ficción'),
    ('Romance', 'Romance'),
    ('Misterio', 'Misterio'),
    ('Fantasía', 'Fantasía'),
    ('Aventura', 'Aventura'),
    ('Drama', 'Drama'),
    ('Terror', 'Terror'),
    ('Biografía', 'Biografía'),
    ('Autoayuda', 'Autoayuda'),
    ('Histórico', 'Histórico'),
    ('Infantil', 'Infantil'),
    )
    genero = models.CharField(max_length=200, choices=GENERO_CHOICES, blank=False, null=False)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    IDIOMA_CHOICES = (
    ('Español', 'Español'),
    ('Ingles', 'Ingles'),
    ('Italiano', 'Misterio'),
    ('Braille', 'Braille'),
    ('Latín', 'Latín'),
    ('Alemán', 'Alemán'),
    ('Francés', 'Francés'),
    ('Portugués', 'Portugués'),
    ('Chino', 'Chino'),
    ('Japonés', 'Japonés'),
    ('Ruso', 'Ruso'),
    ('Árabe', 'Árabe'),
    )
    idioma = models.CharField(max_length=100,choices= IDIOMA_CHOICES, blank=False, null=False)
    numero_de_paginas = models.PositiveIntegerField(blank=True, null=True)
    disponible = models.BooleanField(default=True)
    fecha_de_entrada = models.DateField(default = timezone.now)

    def __str__(self):
        return self.titulo