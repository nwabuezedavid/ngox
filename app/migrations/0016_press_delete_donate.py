# Generated by Django 5.0.4 on 2024-10-31 18:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_bankdetail_additional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('uuids', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('view', models.IntegerField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='donate',
        ),
    ]
