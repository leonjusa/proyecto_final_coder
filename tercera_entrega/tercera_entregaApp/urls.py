from django.contrib import admin
from django.urls import path
from tercera_entregaApp.views import *
from django.contrib.auth.views import LogoutView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
   path('', inicio, name="inicio"),
   path('empleadoformulario/', empleadoFormulario, name="empleadoformulario"),
   path('clienteformulario/', clienteFormulario, name="clienteformulario"),
   path('cafeformulario/', cafeFormulario, name="cafeformulario"),
   path('busquedacliente/', busquedaCliente, name="busquedacliente"),
   path('buscar/', buscar, name="Buscar"),
   path('listacafe/', staff_member_required(Listacafe.as_view(), redirect_field_name='/tercera_entregaApp/noaut/'), name="listacafe"),
   path('cafedetail/<pk>/', Cafedetail.as_view(), name="cafedetail"),
   path('cafecreate/', Cafecreate.as_view(), name="cafecreate"),
   path('cafeupdate/<pk>/', Cafeupdate.as_view(), name="cafeupdate"),
   path('cafedelete/<pk>/', Cafedelete.as_view(), name="cafedelete"),
   path('login/', loginV, name="login"),
   path('registro/', register, name="registro"),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
   path('editarperfil/', editarperfil, name="editarperfil"),
   path('about/', About, name='about'),
   path('noaut/', Noaut, name="noaut"),

]