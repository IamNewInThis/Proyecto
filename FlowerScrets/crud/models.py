from distutils.command.upload import upload
from hashlib import blake2b
from tabnanny import verbose
from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=50,verbose_name='Categoria')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        ordering=['-categoria']

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,max_length=5,verbose_name='ID')
    nombre =  models.CharField(max_length=20,verbose_name='Nombre')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True,blank=True)
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Precio')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['idProducto']

    def __str__(self):
        return self.nombre