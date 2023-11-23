from django.contrib import admin
from .models import Colección
# Register your models here.

class Colección_admin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'disponible',)
    search_fields = ('titulo', 'autor', 'genero', 'disponible',)


admin.site.register(Colección, Colección_admin)