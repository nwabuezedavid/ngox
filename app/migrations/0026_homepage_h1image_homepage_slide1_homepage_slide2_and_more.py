# Generated by Django 5.0.4 on 2024-11-01 08:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_remove_homepage_h1image_remove_homepage_slide1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='h1image',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slide1',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slide2',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slide3',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slide4',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slide5',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='uuids',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
