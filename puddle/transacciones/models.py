from django.db import models
from item.models import Item
# Create your models here.

class Transaccion(models.Model):
    ## datos de referencia
    #usuario = models.ForeignKey(User,related_name='items'), on_delete=models.SET_NULL,null=True,blank=True)
    #created_by = models.ForeignKey(User,related_name='items',on_delete = models.CASCADE)
    monto = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='transacciones', null=False, blank=True)
    moneda = models.CharField(max_length=5,default='COP')

    
    ## datos de la tarjeta (inseguros) que miedo
    PAN_1 = models.CharField(max_length=4,  null=False)
    PAN_2 = models.CharField(max_length=4, null=False)
    PAN_3 = models.CharField(max_length=4,  null=False)
    PAN_4 = models.CharField(max_length=4, null=False)
    CVS = models.CharField(max_length=3, null=False)
    EXP_M = models.CharField(max_length=2, null=False)
    EXP_Y = models.CharField(max_length=2 ,null=False)

    #CVS =  models.DecimalField(max_digits=3, decimal_places=0)

    # datos de la tarjeta seguros
    titular = models.CharField(max_length=100)
    ultimos_4_digitos = models.CharField(max_length=4)
    marca_tarjeta = models.CharField(max_length=20,blank=True,null=True)
    
    # direccion de facturacion
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    pais = models.CharField(max_length=255,default='Colombia')


    # info pasarela de pagos
    id_transaccion_externa  = models.CharField(max_length=100,blank=True,null=True)
    estado = models.CharField(max_length=20,default='pendiete')

    # Tiempos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f'transaccion #{self.id} | {self.estado} | { self.monto } | {self.moneda} | {self.fecha_creacion}'

    
