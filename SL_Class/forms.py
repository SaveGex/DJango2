from django import forms
from django.utils.translation import gettext_lazy as _
from Solo_Leveling.models import GVideo

class Create(forms.ModelForm):
    class Meta:
        model = GVideo
        exclude = ['publish_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-label'}),
            'comment_video': forms.Textarea(attrs={'class': 'form-control form-label', 'rows': 3}),
            'url_video': forms.TextInput(attrs={'class': 'form-control form-label'}),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

