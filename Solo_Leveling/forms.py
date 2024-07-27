from django import forms
from .models import GVideo

class Create(forms.ModelForm):

    class Meta:
        model = GVideo
        fields = ['name', 'comment_video', 'url_video']