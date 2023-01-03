from django import forms
from .models import fichas, equipamentos, pericias, aventuras
from django.core.exceptions import ValidationError


class NovaFicha(forms.ModelForm):
    class Meta:
        model = fichas
        fields = [
            'nomePersonagem', 'historiaPersonagem', 'id_aventura', 'conter_pericia','possuir_equipamento'
        ]

        widgets = {
            'nomePersomagem': forms.TextInput(attrs={'required': True,'maxlength': 45}),
            'historiaPersonagem': forms.Textarea(attrs={'rows': 3, 'maxlength': 1000}),
            'id_aventura': forms.Select(attrs={'required': True,'class': 'form-group'}),
            'conter_pericia': forms.CheckboxSelectMultiple(attrs={'class': 'form-group'}),
            'possuir_equipamento': forms.CheckboxSelectMultiple(attrs={'class': 'form-group'}),

        }


class NovaAventura(forms.ModelForm):
    class Meta:
        model = aventuras
        fields = [
            'nomeAventura', 'guia_de_ambiente', 'historia_aventura'
        ]

