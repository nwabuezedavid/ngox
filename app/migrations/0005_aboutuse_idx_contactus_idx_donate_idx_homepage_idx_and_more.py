# Generated by Django 5.0.4 on 2024-10-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_job_body_alter_homepage_uuids'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuse',
            name='idx',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='contactus',
            name='idx',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='donate',
            name='idx',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='homepage',
            name='idx',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='idx',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='news',
            name='idx',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='stayupdated',
            name='idx',
            field=models.IntegerField(default=1),
        ),
    ]
