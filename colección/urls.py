from django.urls import path
from . import views

app_name = 'colección'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('<letra>', views.listar, name='listar'),
    path('crear/', views.crear, name='crear' ),
    path('detallar/<int:id>', views.detallar, name='detallar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('borrar/<int:id>/confirmar/', views.borrar_confirm, name='borrar_confirm'),
]



