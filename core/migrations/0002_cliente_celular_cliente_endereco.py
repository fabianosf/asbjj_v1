# Generated by Django 5.0 on 2023-12-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="celular",
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="endereco",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
