# Generated by Django 5.0.4 on 2024-10-31 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_press_delete_donate'),
    ]

    operations = [
        migrations.AddField(
            model_name='press',
            name='cdate',
            field=models.DateField(blank=True, max_length=500, null=True),
        ),
    ]