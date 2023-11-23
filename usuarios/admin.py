from django.contrib import admin
from .models import Usuarios, Prestamos

# Register your models here.

class Usuarios_admin(admin.ModelAdmin):
    exclude = ('fecha_de_registro','adeuda','historial_de_prestamos',)
    list_display = ('nombre', 'apellido', 'fecha_de_registro', 'mostrar_historial_de_prestamos',)
    search_fields = ('nombre', 'apellido', 'fecha_de_registro',)
    
    def mostrar_historial_de_prestamos(self, obj):
        return ', '.join([str(prestamo) for prestamo in obj.historial_de_prestamos.all()])

    mostrar_historial_de_prestamos.short_description = 'Historial de Préstamos'


class Prestamos_admin(admin.ModelAdmin):
    exclude = ('fecha_de_prestamo',)
    list_display = ('usuario', 'fecha_de_prestamo', 'fecha_de_devolucion', 'mostrar_libros_prestados')
    search_fields = ('usuario', 'fecha_de_prestamo', 'fecha_de_devolucion')

    def mostrar_libros_prestados(self, obj):
        return ', '.join([str(libro) for libro in obj.libros.all()])
    
    mostrar_libros_prestados.short_description = 'libros_prestados'


admin.site.register(Usuarios, Usuarios_admin)
admin.site.register(Prestamos, Prestamos_admin)



        