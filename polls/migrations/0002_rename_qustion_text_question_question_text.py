# Generated by Django 5.0.7 on 2024-07-22 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='qustion_text',
            new_name='question_text',
        ),
    ]
