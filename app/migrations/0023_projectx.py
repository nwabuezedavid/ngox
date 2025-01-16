# Generated by Django 5.0.4 on 2024-11-01 07:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_publications_publicationsx'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectx',
            fields=[
                ('uuids', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('state', models.CharField(blank=True, max_length=500, null=True)),
                ('Status', models.CharField(blank=True, max_length=500, null=True)),
                ('TYPE', models.CharField(blank=True, max_length=500, null=True)),
                ('author', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('image1', models.TextField(blank=True, null=True)),
                ('image2', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]