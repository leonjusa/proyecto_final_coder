from django import forms

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
    

