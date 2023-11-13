# Generated by Django 4.2.6 on 2023-11-11 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
        ),
        migrations.CreateModel(
            name="CarBrand",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("brand", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="CarModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("model", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="CarConfiguration",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("сolor", models.CharField(max_length=20)),
                ("wheel", models.CharField(max_length=20)),
                ("engine", models.CharField(max_length=20)),
                ("cars", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="car.car")),
            ],
        ),
        migrations.AddField(
            model_name="car",
            name="brand",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="car.carbrand"),
        ),
        migrations.AddField(
            model_name="car",
            name="name",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="car.carmodel"),
        ),
    ]
