from django.contrib import admin
from django.urls import path
from tercera_entregaApp.views import *

urlpatterns = [
   path('', inicio, name="inicio"),
   path('empleados/', empleados, name="Empleados"), 
   path('cafe/', cafe, name="Cafe"),
   path('clientes/', clientes, name="clientes"),
   path('empleadoformulario/', empleadoFormulario, name="empleadoformulario")

]