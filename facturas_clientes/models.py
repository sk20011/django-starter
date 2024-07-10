from django.db import models

class Cliente(models.Model):
    TIPO_OPCIONES = [
        ("particular", "Particular"),
        ("empresa", "Empresa")
    ]
    nombre = models.CharField(max_length=42)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=255)
    NIF = models.CharField(max_length=12)
    tipo = models.CharField(max_length=12, choices=TIPO_OPCIONES, default="particular")
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Factura(models.Model):
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, default=21)  # El % en decimal
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Factura #{self.id} - {self.cliente.nombre}"
