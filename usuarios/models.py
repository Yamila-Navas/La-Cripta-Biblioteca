from django.db import models
from colección.models import Colección
from django.utils import timezone

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    mail = models.EmailField(blank=False, null=False)
    tel = models.CharField(max_length=50, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=False, null=False)
    fecha_de_registro= models.DateField(default=timezone.now)
    historial_de_prestamos = models.ManyToManyField('Prestamos', blank=True)
    adeuda = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Prestamos(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete= models.CASCADE)
    libros = models.ManyToManyField(Colección, related_name='prestamos')
    fecha_de_prestamo = models.DateField(default = timezone.now)
    fecha_de_devolucion = models.DateField(blank=False, null=False)
    devuelto = models.BooleanField(default=False)
    
    def __str__(self):
        libros_str = ', '.join(libro.titulo for libro in self.libros.all())
        return f'{self.usuario} - Libros: {libros_str} - {self.fecha_de_prestamo}'

        












    
    
