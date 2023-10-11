from rest_framework import serializers

from comment.models import Comment
from user.serializers import ShortUserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
