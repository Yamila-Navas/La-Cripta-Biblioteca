from django.db import transaction
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse

from colección.forms import Colección_form
from .models import Usuarios, Prestamos, Colección
from .forms import Usuario_Form, Prestamos_Form
from django.contrib import messages

def listar(request, letra = None):
    if letra != None:
        usuarios = Usuarios.objects.filter(nombre__istartswith = letra)
    else:
        usuarios = Usuarios.objects.filter(nombre__contains = request.GET.get('search', ''))

    contexto = {
        'usuarios' : usuarios
    }

    return render(request, 'usuarios/view.html', contexto)


def crear(request):
    if request.method == 'POST':
        form = Usuario_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar')
    else:
        form = Usuario_Form()
    
    contexto = {
        'form' : form
    }

    return render(request, 'usuarios/create.html', contexto)


def editar(request, id):
    usuario = Usuarios.objects.get(id=id)
    if request.method == 'POST':
        form = Usuario_Form(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            #messages.success(request, "Informacion actualizada.")
            return redirect('usuarios:listar')
    else:
        form = Usuario_Form(instance=usuario)

    contexto = {
        'form': form,
        'id':id
    }
    return render(request, 'usuarios/edit.html', contexto)
    

def confirmacionBorrar(request, id):
    usuario = Usuarios.objects.get(id=id)
    contexto = {
        'usuario':usuario
    }
    return render(request, 'usuarios/delete_confirm.html', contexto)


def borrar(request, id):
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios:listar')


def borrarYDevolverLibro(req, id):
    usuario = get_object_or_404(Usuarios, id=id)
    #devolver los libros prestados al usuario por borrar:
    prestamos = Prestamos.objects.filter(usuario=usuario , devuelto=False)

    with transaction.atomic():
        for prestamo in prestamos:
            for libro in prestamo.libros.all():
                libro.disponible = True
                libro.save()

        usuario.delete()


    return redirect('usuarios:listar')



def buscar_libros(request):
    term = request.GET.get('term', '')
    libros = Colección.objects.filter(titulo__icontains=term, disponible=True)
    results = [{'id': libro.id, 'text': libro.titulo} for libro in libros]
    
    return JsonResponse({'results': results})


def detallar(request, id):
    usuario = Usuarios.objects.get(id = id)

    if request.method == 'POST':
        form = Prestamos_Form(request.POST)
        if form.is_valid():
            form.save()
            with transaction.atomic():
                #Obtengo los libros seleccionados y actualizo el campo 'disponible'
                libros_seleccionados = form.cleaned_data['libros']
                for libro in libros_seleccionados:
                    libro.disponible = False
                    libro.save()

                #modifica el campo adeuda de el usuario cuando se lleva un libro:
                usuario.adeuda = True
                usuario.save()

                return redirect('usuarios:detallar', id=usuario.id)
    else:
        form = Prestamos_Form(initial={'usuario': usuario})
        

    prestamos = Prestamos.objects.filter(usuario__id=id)
    
    contexto = {
        'usuario': usuario,
        'prestamos': prestamos,
        'form' : form,
        'id' : id
    }

    return render(request, 'usuarios/detail.html', contexto)



def devolver(req, id):
    prestamo = get_object_or_404(Prestamos, id=id)
    usuarioId = prestamo.usuario.id
    # Uso transaction.atomic() para asegurar operaciones atómicas
    with transaction.atomic():
        prestamo.devuelto = True
        prestamo.save()

        libros_devueltos = prestamo.libros.all()
        for libro in libros_devueltos:
            libro.disponible = True
            libro.save()
        
        #aca cuando el usuario devuelva todos los libros ya no va a apareser que adeuda
        otros_prestamos_pendientes = Prestamos.objects.filter(usuario=prestamo.usuario, devuelto=False).exists()
        usuario = Usuarios.objects.get(id=usuarioId)
        usuario.adeuda = otros_prestamos_pendientes
        usuario.save()
        
    
    return redirect('usuarios:detallar', id=usuarioId)

