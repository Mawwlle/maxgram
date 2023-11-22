from rest_framework import serializers

from post.models import Post
from user.serializers import ShortUserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)
    text = serializers.CharField(write_only=True)

    class Meta:
        model = Post
        fields = "__all__"
