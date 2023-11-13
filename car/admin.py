from django.contrib import admin

from car.models import Car, CarBrand, CarConfiguration, CarConfigurationOrder, CarModel, Purchase

# Register your models here.
admin.site.register((Car, CarBrand, CarModel, CarConfiguration, CarConfigurationOrder, Purchase))
