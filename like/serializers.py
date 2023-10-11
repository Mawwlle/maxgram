from rest_framework import serializers

from like.models import Like
from user.serializers import ShortUserSerializer


class LikeSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = "__all__"
