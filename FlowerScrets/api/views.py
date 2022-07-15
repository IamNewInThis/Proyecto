from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from crud.models import *
from core.models import *
from .serializers import *

#PRODUCTO
@api_view(['GET','POST','DELETE']) #tipo de llamas que va a recibir
def productos_list(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        productos_serializer = ProductoSerializer(productos,many=True)
        return Response(productos_serializer.data)

    elif request.method == 'POST':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data,status=status.HTTP_201_CREATED)
        return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cantidad = Producto.objects.all().delete()
        return Response({'mensaje':'{} productos han sido eliminados de la base de datos.'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def productos_detail(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
    except:
        return Response({'mensaje':'El producto no existe'},status=status.HTTP_404_NOT_FOUND)
    
    #OBTENER PRODUCTO POR ID
    if request.method == 'GET':
        producto_serializer = ProductoSerializer(producto)
        return Response(producto_serializer.data)

    elif request.method == 'PUT':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(producto,data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#CATEGORIA
@api_view(['GET','POST'])
def categoria_list(request):

    if request.method == 'GET':
        categorias = Categoria.objects.all().order_by('id')
        categorias_serializer = CategoriaSerializer(categorias,many=True)
        return Response(categorias_serializer.data)

    elif request.method == 'POST':
        categoria_data = JSONParser().parse(request)
        categoria_serializer = CategoriaSerializer(data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response(categoria_serializer.data,status=status.HTTP_201_CREATED)
        return Response(categoria_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cantidad = Producto.objects.all().delete()
        return Response({'mensaje':'{} productos han sido eliminados de la base de datos.'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

#USUARIOS
@api_view(['GET','POST','DELETE'])
def cuenta_list(request):

    if request.method == 'GET':
        cuentas = Cuenta.objects.all().order_by('id')
        cuentas_serializer = CuentaSerializer(cuentas,many=True)
        return Response(cuentas_serializer.data)
    
    elif request.method == 'POST':
        cuenta_data = JSONParser().parse(request)
        cuenta_serializer = CuentaSerializer(data=cuenta_data)
        if cuenta_serializer.is_valid():
            cuenta_serializer.save()
            return Response(cuenta_serializer.data,status=status.HTTP_201_CREATED)
        return Response(cuenta_serializer.errors, status=status.HTTP_400_BAD_REQUEST)