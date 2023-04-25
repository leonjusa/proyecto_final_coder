from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpleadoFormulario, CafeFormulario, ClienteFormulario
from .models import Empleado, Cliente, Tipo_cafe
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView



def inicio(self):
    
    return render(self, "inicio.html")

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
  
def clienteFormulario(request):
    
    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
      
      miFormulario = ClienteFormulario(request.POST)

      print(miFormulario)

      if miFormulario.is_valid():
          
          data = miFormulario.cleaned_data

          cliente = Cliente(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
          cliente.save()
    
          return render(request, "inicio.html")
    
      else:
          
          return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    
    else:

      miFormulario = ClienteFormulario()

      return render(request, "clienteformulario.html", {"miFormulario": miFormulario})
    
def cafeFormulario(request):
    
    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
      
      miFormulario = CafeFormulario(request.POST)

      print(miFormulario)

      if miFormulario.is_valid():
          
          data = miFormulario.cleaned_data

          cafe = Tipo_cafe(nombre=data['nombre'], tostado=data['tostado'], grano=data['grano'], cantidad_kg=data['cantidad_kg'])
          cafe.save()
    
          return render(request, "inicio.html")
    
      else:
          
          return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    
    else:

      miFormulario = CafeFormulario()

      return render(request, "cafeformulario.html", {"miFormulario": miFormulario})
   
def busquedaCliente(request):

    return render(request, "busquedacliente.html")  

def buscar(request):
  
    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        cliente = Cliente.objects.filter(nombre=nombre)
        return render(request, "resultadosbusqueda.html", {"cliente": cliente, "nombre": nombre})
    
    else:
        return HttpResponse(f'No se recibio informacion')
    
class Listacafe(ListView):
  
  model = Tipo_cafe
  template_name = 'listacafe.html'
  context_object_name = 'cafe'

class Cafedetail(DetailView):
  
  model = Tipo_cafe
  template_name = 'cafedetail.html'
  context_object_name = 'cafedet'

class Cafecreate(CreateView):
   
  model = Cafedetail
  template_name = 'cafecreate.html'
  fields = ['nombre', 'tostado','grano','cantidad']
  success_url = '/app-coder/'
