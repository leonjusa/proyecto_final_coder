from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpleadoFormulario, CafeFormulario, ClienteFormulario, UserEditForm
from .models import Empleado, Cliente, Tipo_cafe, Avatar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test


def inicio(self):
    
    try:
      avatar = Avatar.objects.get(user=self.user.id)
      return render(self, 'inicio.html', {'url': avatar.imagen.url})
    except:
      return render(self, "inicio.html")
    
@staff_member_required(login_url='/tercera_entregaApp/noaut/')
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
   
@staff_member_required(login_url='/tercera_entregaApp/noaut/')
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
  fields = ['nombre', 'tostado','grano','cantidad_kg','imagen',]
  success_url = '/tercera_entregaApp/'

  def form_valid(self, form):
    response = super().form_valid(form)
    if 'imagen' in self.request.FILES:
      self.object.imagen = self.request.FILES['imagen']
      self.object.save()
    return response


class Cafeupdate(UpdateView):
    model = Tipo_cafe
    template_name = 'cafeupdate.html'
    fields = ('nombre', 'tostado', 'grano', 'cantidad_kg', 'imagen')
    success_url = '/tercera_entregaApp/'
    context_object_name = 'cafeup'

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.FILES.get('imagen'):
            self.object.imagen = self.request.FILES['imagen']
            self.object.save()
        return response


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
          usuario.set_password(data["password1"])
          usuario.save()
          
          return render(request, "inicio.html", {"mensaje": "Datos actualizados, vuelve a iniciar sesion"})
    
      else:
          return render(request, "inicio.html", {"miform": miform})
    else:
      miform = UserEditForm(instance=request.user)
      return render(request, "editarPerfil.html", {"miform": miform})
    
def About(request):
    context = {
        'title': 'Acerca de mí',
        'image_url': '/media/fotoleo.jpg',
        'texto': """Mi nombre es Leonardo Laborda.
Nací en Montevideo en el año 1977, desde muy chico sentí atracción por la informática y la electrónica en general, teniendo mis primeros pasos con una Sinclair ZX Septum 48Kb RAM, con ella aprendí de forma autodidacta a programar en Basic.
Estudie Ingeniería electrónica, fotografía, edición cinematográfica, y varios cursos cortos relacionados con las ventas y la informática.
Mi sueño siempre fue estudiar programación “profunda” pero por razones económicas me fue imposible, y para empeorar la situación emigre para Estados Unidos a la edad de 22 años y mi vida a partir de ahí fue dedicada al trabajo y la familia.
En USA realizo trabajos de reparaciones de computadoras, programación de bases de datos en Access, instalación de sistemas de CCTV, me desempeño como fotógrafo y manejo Uber los fines de semana.
Siempre fui muy inquieto por el conocimiento, la lectura es mi pasión y si es sobre ciencia mucho mejor, en los ratos libres leo  sobre: física relativista, mecánica cuántica, astrofísica, e historia.
La Astronomía la cultivo desde muy pequeño, soy miembro de asociaciones relacionadas voy regularmente a observatorios y tengo mi propio telescopio.
Dada la rápida expansión de los trabajos remotos, fue este año que decidí volver a abrir la cabeza al conocimiento y comenzar a estudiar programación y carreras relacionadas.
“Nunca es tarde para reinventarse y evolucionar”

							                    Leonardo Laborda 2023
""",
    }
    return render(request, 'about.html', context)

def Noaut(request):
   return render(request, "noaut.html")
