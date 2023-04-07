from django.contrib import admin
from django.urls import path
from tercera_entregaApp.views import *

urlpatterns = [
   path('', inicio, name="inicio"),
   path('empleadoformulario/', empleadoFormulario, name="empleadoformulario"),
   path('clienteformulario/', clienteFormulario, name="clienteformulario"),
   path('cafeformulario/', cafeFormulario, name="cafeformulario"),
   path('busquedacliente/', busquedaCliente, name="busquedacliente"),
   path('buscar/', buscar, name="Buscar"),

]