# Generated by Django 5.0.4 on 2024-10-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_bankdetail_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='additional',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]