# Generated by Django 5.1.7 on 2025-03-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_ejercicios_rutinas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_trainner",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
