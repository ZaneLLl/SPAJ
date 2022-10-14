from django import forms


class Ficha_form(forms.Form):
    nomep = forms.CharField(label='nomep', max_length=45)
    LVL = forms.IntegerField(label='LVL')
