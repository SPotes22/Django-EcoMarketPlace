from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransaccionForm
from item.models import Item
from django.contrib import messages

def procesar_transaccion(request):
    item_id = request.GET.get('item_id') or request.POST.get('monto')  # lo buscamos por GET o POST
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        print("POST data:", request.POST)
        print("/n","POST data:", request.POST)

        if form.is_valid():
            print("Formulario válido")
            transaccion = form.save(commit=False)
            # detalles 
            transaccion.monto = item
            item = get_object_or_404(Item, id=item_id)
            cantidad = getattr(item, 'cantidad', 1)  # ← por si viene del carrito
            total = item.price * cantidad
            transaccion.total_pagado = total
            
            

            # pago 
            transaccion.estado = 'aprobado'  # ya lo tienes
            transaccion.moneda = 'COP'       # si no viene desde form
            transaccion.pais = 'Colombia'    # si no viene desde form
            transaccion.save()
            # api momento
            print("Transacción guardada:", transaccion)
            messages.success(request, 'Pago procesado correctamente.')
            return redirect('transaccion_exitosa')
        else:
            print("Errores de validación:", form.errors)
    else:
        cantidad = getattr(item, 'cantidad', 1)
        total = item.price * cantidad
        form = TransaccionForm()

    # Pasamos el item como lista de 1 solo para reusar el loop del template
    return render(request, 'transacciones/pago.html', {
        'form': form,
        'total_general': total,
        'items_comprados': [item]
        })




def error_transacciones(request, mensaje="Error al procesar la tarjeta"):
    redirect('error_transaccion')
    return render(request, 'transacciones/error.html', {'error_message': mensaje})

def transaccion_exitosa(request):
    redirect('transaccion_exitosa')
    return render(request, 'transacciones/exito.html')




def pagar_items(request):
    carrito = [
        {'item_id': 1, 'cantidad': 2},
        {'item_id': 3, 'cantidad': 1}
    ]

    items_comprados = []  #  inicialización correcta
    total_general = 0

    for entry in carrito:
        item = Item.objects.get(id=entry['item_id'])
        item.cantidad = entry['cantidad']
        item.subtotal = item.price * item.cantidad
        items_comprados.append(item)
        total_general += item.subtotal  # acumulador manual

    return render(request, 'transacciones/carrito.html', {
        'items_comprados': items_comprados,
        'total_general': total_general
    })



