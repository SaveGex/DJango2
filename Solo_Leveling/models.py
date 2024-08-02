from django.db import models
from django.utils import timezone
# Create your models here.
class GVideo(models.Model):
    name = models.CharField(max_length=100)
    comment_video = models.TextField(default="Comment was skipped", null=True)
    url_video = models.URLField(max_length=500)
    publish_date = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return self.name