# Generated by Django 5.0.7 on 2024-07-27 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solo_Leveling', '0004_remove_gvideo_name_video_gvideo_comment_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gvideo',
            name='comment_video',
            field=models.TextField(default='Comment to video'),
        ),
        migrations.AlterField(
            model_name='gvideo',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 10, 21, 38, 397984, tzinfo=datetime.timezone.utc)),
        ),
    ]
