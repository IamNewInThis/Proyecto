from django import forms
from .models import Cuenta

class cuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['user','rut','fechnac','numte','direcc']
        widgets = {'user':forms.Select(attrs={'class': 'form-control'}),'rut':forms.TextInput(attrs={'class': 'form-control'}),'fechnac':forms.DateInput(attrs={'class': 'form-control'}),'numte':forms.NumberInput(attrs={'class': 'form-control'}),'direcc':forms.TextInput(attrs={'class': 'form-control'})}