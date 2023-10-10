from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("id", "email", "last_login", "is_superuser", "first_name", "last_name", "username", "password")
        read_only_fields = ("last_login", "is_superuser")

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
