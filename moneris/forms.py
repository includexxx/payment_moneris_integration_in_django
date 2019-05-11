from .models import Moneris
from django import forms


class MonerisForm(forms.ModelForm):

    class Meta:
        model = Moneris
        fields = ('name', 'ps_store_id', 'hpp_key', 'access_token', 'environment')