from django import forms
from .models import Alvo


class AlvoForm(forms.ModelForm):
    latitude = forms.FloatField(required=True)

    class Meta:
        model = Alvo
        fields = ['nome', 'latitude', 'longitude', 'data_expiracao']