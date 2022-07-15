from django.shortcuts import render, redirect, reverse

from core.views import flores
from .models import *
from .forms import *
# Create your views here.

def productos_list(request): 
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/productos_list.html',context)

def productos_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            nombre = form.cleaned_data.get("nombre")
            categoria = form.cleaned_data.get("categoria")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            imagen = form.cleaned_data.get("imagen")
            obj = Producto.objects.create(
                idProducto=idProducto,
                nombre=nombre,
                categoria = categoria,
                precio=precio,
                stock=stock,
                imagen=imagen
            )
            obj.save()
            return redirect(reverse('productos-list')+"?OK")
        else:
            return redirect(reverse('productos-list')+"?FAIL")
    else:
        form = ProductoForm
    return render(request,'crud/productos_new.html',{'form':form})

def productos_edit(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            form = ProductoForm(instance=producto)
        else:
            return redirect(reverse('product-list') + "?FAIL")

        if request.method == 'POST':
            form = ProductoForm(request.POST,request.FILES,instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('product-list') + "?SUCCESS")
            else:
                return redirect(reverse('product-edit') + product_id)
        context = {'form':form}
        return render(request,'crud/productos_edit.html',context)
    except:
        return redirect(reverse('productos-list') + "?FAIL")

def productos_delete(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        producto.delete()
        return redirect(reverse('productos-list') + "?DELETED")
    except:
        return redirect(reverse('productos-list') + "?FAIL")

def product_by_categoria(request,categoria):
    productos = Producto.objects.filter(categoria=categoria)
    return render(request,'crud/productos_list.html',{'productos':productos})