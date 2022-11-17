from django import forms
from .models import fichas, equipamentos, pericias, possuir_equipamento
from aventura.models import aventuras
from django.core.exceptions import ValidationError


class fichas(forms.ModelForm):
    class Meta:
        model = fichas
        fields = [
            'nomePersonagem', 'historiaPersonagem', 'id_aventura','Level', 'Sabedoria', 'Agilidade', 'Conhecimento', 'Destreza', 'ConstFisica', 'Percepção', 'Carisma'
        ]
        widgets = {
            'nomePersomagem': forms.TextInput(attrs={'required': True,'maxlength': 45}),
            'historiaPersonagem': forms.Textarea(attrs={'required': False,'rows': 3, 'maxlength': 1000}),
            'id_aventura': forms.Select(attrs={'required': True,'class': 'form-control'}),
            'Level': forms.NumberInput(attrs={'required': True, 'min': 1, 'max':17 }),
            'Sabedoria': forms.NumberInput(attrs={'required': True, 'min': 1, 'max': 17}),
            'Agilidade': forms.NumberInput(attrs={'required': True, 'min': 1, 'max': 17}),
            'Conhecimento': forms.NumberInput(attrs={'required': True, 'min': 1, 'max': 17}),
            'Destreza': forms.NumberInput(attrs={'required': True, 'min': 1, 'max': 17}),
            'ConstFisica': forms.NumberInput(attrs={'required': True, 'min': 1, 'max': 17}),
            'Percepção': forms.NumberInput(attrs={'required': True, 'min': 1, 'max': 17}),
            'Carisma': forms.NumberInput(attrs={'required': True, 'min': 1, 'max': 17}),
        }

    class Media:
        js = ('./templates/scripts/jv.js')


