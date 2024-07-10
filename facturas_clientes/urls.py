from django.urls import path, include
from .views import detalle_cliente, index
from .views import detalle_cliente, detalle_factura, index
urlpatterns = [
    path('facturas_clientes/', index, name ="facturas_clientes"),
    path('clientes/<int:id>', detalle_cliente, name ="clientes"),
    path('facturas/<int:id>', detalle_factura, name="factura"),
]  
