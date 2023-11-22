from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404

from like.models import Like
from like.serializers import LikeSerializer
from user.models import User


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["user", "post"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ["update", "partial_update", "destroy"]:
            queryset = queryset.filter(user=self.request.user.pk)

        return queryset

    def perform_create(self, serializer: LikeSerializer) -> None:
        user = get_object_or_404(User, pk=self.request.user.pk)
        serializer.save(user=user)
