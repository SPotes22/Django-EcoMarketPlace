from django.urls import path
from . import views

urlpatterns = [
    path('pagar/', views.procesar_transaccion, name='procesar_transaccion'),
    path('pagoexitoso/', views.transaccion_exitosa, name='transaccion_exitosa'),
    path('errorpago/',views.error_transacciones , name='error_transaccion'),
    path('carrito/', views.pagar_items , name='carrito'),
]
