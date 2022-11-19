from django import forms
from .models import fichas, equipamentos, pericias, possuir_equipamento
from aventura.models import aventuras
from django.core.exceptions import ValidationError


class NovaFicha(forms.ModelForm):
    class Meta:
        p = (('Pedro', 'pedro'), ('Kaio', 'kaio'))
        model = fichas
        fields = [
            'nomePersonagem', 'historiaPersonagem', 'id_aventura'
        ]
        widgets = {
            'nomePersomagem': forms.TextInput(attrs={'required': True,'maxlength': 45}),
            'historiaPersonagem': forms.Textarea(attrs={'required': False,'rows': 3, 'maxlength': 1000}),
            'id_aventura': forms.Select(attrs={'required': True,'class': 'form-control'}),

        }

    class Media:
        js = ('./templates/scripts/jv.js')


