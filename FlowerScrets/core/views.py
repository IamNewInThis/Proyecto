from django.shortcuts import render, redirect
from django.http import HttpResponse

#CREAR UN CONSTRUCTOR
class persona:
    def __init__(self, nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad


# Create your views here.

def root(request):
    return redirect('/home')

def home(request):

    #parecido a un json - recibe un objeto, lista, string, numero
    #actor = persona("Brad Pitt","58")
    #lista = ["Aladin","Los Increibles","Frozen"]
    #datos = {"nombre":"Mundo", "peliculas":lista ,"actor":actor}
    return render (request,'core/home.html')#,datos)

def maceteros(request):
    return render(request,'core/maceteros.html')

def flores(request):
    return render(request,'core/flores.html')

def subscripcion(request):
    return render(request,'core/subscripcion.html')

def tierra(request):
    return render(request,'core/tierra.html')

def arbustos(request):
    return render(request,'core/arbustos.html')

def registro(request):
    return render(request,'core/Registro.html')



