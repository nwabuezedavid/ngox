# Generated by Django 5.0.4 on 2024-11-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_homepage_h1image_homepage_slide1_homepage_slide2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuse',
            name='Associationimage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='body2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='ourvision',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='slideH5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='slideh2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='slideh3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='slideh4',
            field=models.TextField(blank=True, null=True),
        ),
    ]