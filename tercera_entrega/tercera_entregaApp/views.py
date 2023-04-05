from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpleadoFormulario
from .models import Empleado

# Create your views here.

def inicio(self):
    
    return render(self, "inicio.html")

def empleados(self):
    
    return render(self, "empleados.html")

def cafe(self):
    
    return render(self, "cafe.html")

def clientes(self):
    
    return render(self, "clientes.html")

def empleadoFormulario(request):
    
    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
      
      miFormulario = EmpleadoFormulario(request.POST)

      print(miFormulario)

      if miFormulario.is_valid():
          
          data = miFormulario.cleaned_data

          empleado = Empleado(nombre=data['nombre'], apellido=data['apellido'], cargo=data['cargo'])
          empleado.save()
    
          return render(request, "inicio.html")
    
      else:
          
          return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    
    else:

      miFormulario = EmpleadoFormulario()

      return render(request, "empleadoformulario.html", {"miFormulario": miFormulario})