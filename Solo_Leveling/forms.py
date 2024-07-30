from django import forms
from django.utils.translation import gettext_lazy as _
from .models import GVideo

class Create(forms.ModelForm):

    class Meta:
        model = GVideo
        exclude = ['publish_date']
        error_messages = {
            "name": {
                "max_length": _("This writer's name is too long."),
            },
        }

