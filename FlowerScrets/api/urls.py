from django.urls import path
from .views import *

urlpatterns =[
    path('productos/',productos_list),
    path('categorias/',categoria_list),
    path('cuentas/',cuenta_list),
    path('productos/<str:product_id>',productos_detail),
]