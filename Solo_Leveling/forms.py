from django import forms
from django.utils.translation import gettext_lazy as _
from .models import GVideo

class Create(forms.ModelForm):

    class Meta:
        model = GVideo
        fields = ["name", "comment_video", "url_video"]
        labels = {
            "name": _("Name of the video"),
            "comment_video": _("Comment to the video"),
            "url_video": _("URL to the video"),
        }
        help_texts = {
            "name": _("Enter the name of the video."),
            "comment_video": _("Provide your comment to the video."),
        }
        error_messages = {
            "name": {
                "max_length": _("The name is too long."),
                "required": _("This field is required."),
            },
            "url_video": {
                "required": _("This field is required."),
            }
        }
