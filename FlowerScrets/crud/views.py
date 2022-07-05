from importlib.resources import contents
from django.shortcuts import render
from .models import *
# Create your views here.

def product_list(request): 
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/productos.html',contents)