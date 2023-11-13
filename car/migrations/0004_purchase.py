# Generated by Django 4.2.6 on 2023-11-11 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("car", "0003_rename_cars_carconfiguration_car_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Purchase",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("buyer_first_name", models.CharField(max_length=150)),
                ("buyer_second_name", models.CharField(max_length=150)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "configuration",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="car.carconfiguration"),
                ),
            ],
        ),
    ]