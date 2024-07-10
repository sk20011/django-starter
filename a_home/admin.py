from django.contrib import admin

from facturas_clientes.models import Cliente, Factura

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Factura)