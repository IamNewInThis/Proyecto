from dataclasses import fields
from django import forms
from django.forms import ModelForm, widgets
from .models import *

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'nombre',
            'categoria',
            'precio',
            'stock',
            'imagen'
        ]
        labels = {
            'idProducto':'Código Producto',
            'nombre':'Nombre',
            'categoria':'Categoria',
            'precio':'Precio',
            'stock':'Stock',            
            'imagen':'Imagen',            
        }
        widgets = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'})
        }