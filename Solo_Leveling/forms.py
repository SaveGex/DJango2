from django import forms
from .models import GVideo

class Create(forms.ModelForm):

    class Meta:
        model = GVideo
        exclude = ['publish_date']
        defaults = {
        'comment_video': 'Comment on video ' + str(GVideo.objects.count() + 1),
        'name': "Name" + str(GVideo.objects.count() + 1),
        }

