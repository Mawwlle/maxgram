from rest_framework import serializers

from car.models import Car, CarConfiguration, CarConfigurationOrder, Purchase
from user.serializers import ShortUserSerializer


class CarConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarConfiguration
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.brand")
    name = serializers.CharField(source="name.model")

    class Meta:
        model = Car
        fields = "__all__"


class CarConfigurationOrderSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = CarConfigurationOrder
        fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"
