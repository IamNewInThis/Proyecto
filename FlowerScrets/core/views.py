from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud.models import *
from django.contrib.auth import authenticate,login,logout as django_logout
from django.contrib import messages
#SE AGREGO
from django.contrib.auth.models import User
from core.models import Cuenta 

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
    context = {'maceteros':Producto.objects.all()}
    return render(request,'core/maceteros.html',context)

def maceteros_by_categoria(request,categoria):
    maceteros = Producto.objects.filter(categoria=categoria)
    return render(request,'core/flores.html',{'maceteros':maceteros})
    
def flores(request):
    context = {'flores':Producto.objects.all()}
    return render(request,'core/flores.html',context)

def flores_by_categoria(request,categoria):
    flores = Producto.objects.filter(categoria=categoria)
    return render(request,'core/flores.html',{'flores':flores})

def subscripcion(request):
    return render(request,'core/subscripcion.html')

def tierra(request):
    return render(request,'core/tierra.html')

def arbustos(request):
    return render(request,'core/arbustos.html')

def registro(request):
    if request.method=='POST':
        newusu = User.objects.create_user(username=request.POST['email'],email=request.POST['email'],password=request.POST['password'],first_name=request.POST['nombre'],last_name=request.POST['apellido'])
        ##usuario = User.objects.create_user(username='pepe',email='corneta@duoc.cl',password='elmaricon123')
        cuenta = Cuenta.objects.create(rut=request.POST['rut'],fechnac=request.POST['fechnac'],direcc=request.POST['direcc'],user_id=newusu.id,numte=request.POST['numte'])
       ##cuenta = Cuenta.objects.create(rut='20146051-4',fechnac='2022-06-22',direcc='av siempre viva',user_id=usuario.id,numte=74341877))
    return render(request,'core/Registro.html')

def logeo(request):
    if request.method=='POST':
        user= authenticate(username=request.POST['correo_login'],password=request.POST['password_login'])
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, "USUARIO NO REGISTRADO O DATOS INCORRECTOS :V")
            return redirect('logeo')
    return render(request,'core/logeo.html')

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('home')
