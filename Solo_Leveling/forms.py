from django import forms
from .models import GVideo

class Create(forms.ModelForm):

    class Meta:
        model = GVideo
        fields = ['name', 'url_video', 'comment_video']