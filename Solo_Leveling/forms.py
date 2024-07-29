from django import forms
from .models import GVideo

class Create(forms.ModelForm):

    class Meta:
        model = GVideo
        exclude = ['publish_date']