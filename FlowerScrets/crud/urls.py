from django.urls import path
from .views import *

urlpatterns = [
    path('',productos_list,name='productos-list'),
    path('new/',productos_new,name='productos-new'),
    path('<str:product_id>/edit',productos_edit,name='productos-edit'),
    path('<str:product_id>/delete',productos_delete,name='productos-delete'),
    path('marca/<str:marca>/',product_by_categoria,name='productos-categoria'),
]