from django import forms

from .models import Thema

class FormThemen(forms.Form):
    
    thema = forms.ModelChoiceField(queryset=Thema.objects.all())
   