# Generated by Django 4.2.6 on 2023-11-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("car", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carconfiguration",
            name="will_arrive",
            field=models.DateField(null=True, verbose_name="Дата прибытия автомобиля"),
        ),
    ]