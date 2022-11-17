from django import forms
from .models import fichas, equipamentos, pericias, possuir_equipamento
from aventura.models import aventuras
from django.core.exceptions import ValidationError


class aventuras(forms.ModelForm):
    class Meta:
        model = aventuras
        fields = ['nomeAventura']
        widgets = {
            'nomeAventura': forms.Select(attrs={'class': 'form-control'})
        }