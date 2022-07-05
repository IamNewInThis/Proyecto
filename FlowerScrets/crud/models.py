from pyexpat import model
from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,max_length=5,verbose_name='ID')
    categoria = models.CharField(max_length=20,verbose_name='Categoria  ')
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Precio')
    