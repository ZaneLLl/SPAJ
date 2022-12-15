from django import forms
from .models import fichas, equipamentos, pericias, possuir_equipamento
from aventura.models import aventuras
from django.core.exceptions import ValidationError


class NovaFicha(forms.ModelForm):
    class Meta:
        model = fichas
        fields = [
            'nomePersonagem', 'historiaPersonagem', 'id_aventura'
        ]
        widgets = {
            'nomePersomagem': forms.TextInput(attrs={'required': True,'maxlength': 45}),
            'historiaPersonagem': forms.Textarea(attrs={'required': False,'rows': 3, 'maxlength': 1000}),
            'id_aventura': forms.Select(attrs={'required': True,'class': 'form-control'}),

        }

class NovaPericia(forms.ModelForm):
    class Meta:
        model = pericias
        fields = [
            'nome_pericia', 'descrição_pericia'
        ]
        widgets = {
            'nome_pericia': forms.TextInput(attrs={'required': True,'maxlength': 45}),
            'descrição_pericia': forms.Textarea(attrs={'rows': 3, 'maxlength': 1000})
        }



