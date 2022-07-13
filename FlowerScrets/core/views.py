from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from core.models import Cuenta 
from core.forms import cuentaForm

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
    if request.method=='POST':
        usuario = User.objects.create_user(username='pepe',email='corneta@duoc.cl',password='elmaricon123')
        cuenta = Cuenta.objects.create(rut='20146051-4',fechnac='2022-06-22',direcc='av siempre viva',user_id=usuario.id,numte=74341877)
        print(usuario)
        print(cuenta)
    return render(request,'core/Registro.html')





