from django.urls import path
from . import views 

app_name = 'usuarios'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('<letra>', views.listar, name='listar'),
    path('crear/', views.crear, name='crear'),
    path('detallar/<int:id>', views.detallar, name='detallar'),
    path('buscar_libros/', views.buscar_libros, name='buscar_libros'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('confirmacion-borrar/<int:id>', views.confirmacionBorrar, name='confirmacion-borrar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('borrarYDevolverLibro/<int:id>', views.borrarYDevolverLibro, name='borrarYDevolverLibro'), #
    path('devolver/<int:id>', views.devolver, name='devolver'),

]
