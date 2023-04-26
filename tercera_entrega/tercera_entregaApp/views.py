from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpleadoFormulario, CafeFormulario, ClienteFormulario, UserEditForm
from .models import Empleado, Cliente, Tipo_cafe
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
    
class Listacafe(LoginRequiredMixin, ListView):
  
  model = Tipo_cafe
  template_name = 'listacafe.html'
  context_object_name = 'cafe'

class Cafedetail(DetailView):
  
  model = Tipo_cafe
  template_name = 'cafedetail.html'
  context_object_name = 'cafedet'

class Cafecreate(CreateView):
   
  model = Tipo_cafe
  template_name = 'cafecreate.html'
  fields = ['nombre', 'tostado','grano','cantidad_kg']
  success_url = '/tercera_entregaApp/'

class Cafeupdate(UpdateView):
   
  model = Tipo_cafe
  template_name = 'cafeupdate.html'
  fields = ('__all__')
  success_url = '/tercera_entregaApp/'
  context_object_name = 'cafeup'

class Cafedelete(DeleteView):
   
   model = Tipo_cafe
   template_name = 'cafedelete.html'
   success_url = '/tercera_entregaApp/'

def loginV(request):
   
  if request.method == 'POST':
    miform = AuthenticationForm(request, data=request.POST)

    if miform.is_valid():
        
      data = miform.cleaned_data
      usuario = data["username"]
      psw = data["password"]
      
      user = authenticate(username=usuario, password=psw)

      if user:
        login(request, user)
        return render(request, 'inicio.html', {"mensaje": f'Bienvenido {usuario}'})
      
      else:
        return render(request, 'inicio.html', {"mensaje": f'Formulario invalido'})
         
    else:
      return render(request, "inicio.html", {"mensaje": "Usuario o contraseña inexistente!"})
  else:
    miform = AuthenticationForm()
    return render(request, "login.html", {"miform": miform})
  
def register(request):
   
  if request.method == 'POST':
    miform = UserCreationForm(request.POST)

    if miform.is_valid():
        
      data = miform.cleaned_data
      username = data["username"]
      miform.save()
      return render(request, 'inicio.html', {"mensaje": f'Usuario {username} creado!'})
         
    else:
      return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
  
  else:
    miform = UserCreationForm()
    return render(request, "registro.html", {"miform": miform})  
  
@login_required
def editarperfil(request):

    usuario = request.user

    if request.method == 'POST':
      
      miform = UserEditForm(request.POST, instance=request.user)

      if miform.is_valid():
          data = miform.cleaned_data
          usuario.email = data['email']
          usuario.first_name = data['first_name']
          usuario.last_name = data['last_name']
          usuario.save()
          
          return render(request, "inicio.html", {"mensaje": "Datos actualizados!"})
    
      else:
          return render(request, "inicio.html", {"miform": miform})
    else:
      miform = UserEditForm(instance=request.user)
      return render(request, "editarPerfil.html", {"miform": miform})
    
