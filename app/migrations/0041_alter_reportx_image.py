# Generated by Django 5.0.4 on 2024-11-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_alter_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportx',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
