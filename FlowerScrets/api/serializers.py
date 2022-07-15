from dataclasses import field
from rest_framework import serializers
from crud.models import Producto, Categoria
from core.models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto','nombre','categoria','precio','stock')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','categoria')

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('rut','numte','direcc')