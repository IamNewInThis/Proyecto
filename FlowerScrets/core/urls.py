from django.urls import path

from crud.views import product_by_categoria
from .views import *


urlpatterns = [
    path('',root),
    path('home', home,name="home"),

    path('maceteros',maceteros,name="maceteros"),
    path('maceteros/<int:categoria>',product_by_categoria,name="productos-categoria"),

    path('flores',flores,name="flores"),
    path('flores/<int:categoria>',product_by_categoria,name="productos-categoria"),

    path('tierra',tierra,name="tierra"),
    path('subscripcion',subscripcion,name="subscripcion"),
    path('arbustos',arbustos,name="arbustos"),
    path('registro',registro,name="registro"),

    path('logeo',logeo,name="logeo"),
    path('logout',logout,name="logout"),

    path('agregar/<str:idProducto>/', agregar_producto, name="Add"),
    path('eliminar/<str:idProducto>/', eliminar_producto, name="Del"),
    path('restar/<str:idProducto>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]