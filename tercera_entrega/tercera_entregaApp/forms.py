from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Tipo_cafe


class EmpleadoFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    cargo = forms.CharField()

class CafeFormulario(forms.Form):
    
    nombre = forms.CharField()
    tostado = forms.CharField()
    grano = forms.CharField()
    cantidad_kg = forms.IntegerField()

class ClienteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class UserEditForm(UserChangeForm):
   
  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
  )

  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  class Meta:
    model=User
    fields=('email', 'first_name', 'last_name','password1','password2')

  def clean_password2(self):

    print(self.cleaned_data)

    password2 = self.cleaned_data["password2"]
    if password2 != self.cleaned_data["password1"]:
      raise forms.ValidationError("Las contraseñas no coinciden!")
    return password2
  
class TipoCafeForm(forms.ModelForm):
    class Meta:
        model = Tipo_cafe
        fields = ('nombre', 'tostado', 'grano', 'cantidad_kg', 'imagen')