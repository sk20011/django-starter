from django.shortcuts import render
from.models import Cliente, Factura

# Create your views here.
def index(request):
    print("Han solicitado facturas_clientes")
    clientes = list(Cliente.objects.all())
    facturas = list(Factura.objects.all())

    context = {
        "Secret": "Supersafe24",
        "clientes": clientes,
        "facturas": facturas,
    }
    
    return render(request, 'facturas_clientes/index.html', context=context)


def detalle_cliente(request, id):
    cliente = Cliente.objects.all().filter(pk=id).first()
    context = {
        "cliente": cliente,
    }
    return render(request, 'facturas_clientes/clientes.html', context=context)


def detalle_factura(request, id):
    factura = Factura.objects.all().filter(pk=id).first()
    
    context = {
        
        "factura": factura,
    }
    return render(request, 'facturas_clientes/facturas.html', context=context)