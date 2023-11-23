from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .forms import Colección_form
from .models import Colección
from usuarios.models import Prestamos



def listar(request, letra = None):
    if letra != None:
        colección = Colección.objects.filter(titulo__istartswith = letra)
    else:
        colección = Colección.objects.filter(titulo__contains = request.GET.get('search', ''))

    contexto = {
        'colección' : colección
    } 

    return render(request, 'colección/view.html', contexto)


def crear(request):
    if request.method == 'POST':
        form = Colección_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('colección:listar') #revisar porque no anda redirect
    else:
        form = Colección_form()
        
    contexto = {
        'form' : form
    } 
    return render(request, 'colección/create.html', contexto)


def detallar(request, id):
    libro = Colección.objects.get(id=id)

    #si el libro no esta disponible, consulto a quien fue prestado
    '''prestamos = Prestamos.objects.filter(devuelto=False)
    for prestamo in prestamos:
        if prestamo.libros.filter(titulo=libro.titulo):
            libroPrestadoA = f'{prestamo.usuario.nombre}, {prestamo.usuario.apellido}'
            break # esto si ese libro es unico en la biblioteca
        else:
            libroPrestadoA = None'''
    #aca utilizo first() para simplificar el codigo:
    prestamo = Prestamos.objects.filter(devuelto=False, libros__titulo=libro.titulo).first()
    prestadoA = f'{prestamo.usuario.nombre}, {prestamo.usuario.apellido}' if prestamo else None

    contexto = {
        'libro' : libro,
        'prestadoA': prestadoA
    }
    return render(request, 'colección/detail.html', contexto)


def editar(request, id):
    libro = Colección.objects.get(id=id)
    if request.method == 'POST':
        form = Colección_form(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('colección:listar')
    else:
        form = Colección_form(instance=libro)
    
    contexto = {
        'form':form,
        'id':id
    }
    return render(request, 'colección/edit.html', contexto)


def borrar_confirm(request, id):
    libro = get_object_or_404(Colección, id=id)
    contexto = {'libro': libro}
    return render(request, 'colección/delete_confirm.html', contexto)


def borrar(request, id):
    if request.method == 'POST':
        libro = Colección.objects.get(id=id)
        libro.delete()
        return redirect('colección:listar')
    else:
        return redirect('colección:borrar_confirm', id=id)
    


