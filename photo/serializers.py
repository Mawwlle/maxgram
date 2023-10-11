from rest_framework import serializers

from photo.models import Photo
from user.serializers import ShortUserSerializer


class PhotoSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Photo
        fields = "__all__"
