# Generated by Django 5.0.4 on 2024-11-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_alter_job_closedate_alter_job_date_alter_news_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='press',
            name='cdatex',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='press',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectx',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicationsx',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reportx',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
