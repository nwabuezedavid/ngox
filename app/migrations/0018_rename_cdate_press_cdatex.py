# Generated by Django 5.0.4 on 2024-10-31 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_press_cdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='press',
            old_name='cdate',
            new_name='cdatex',
        ),
    ]