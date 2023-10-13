from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from user.permissions import IsOwnerOrAdmin
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self) -> list[permissions.BasePermission]:
        if self.action == "create":
            return []
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]

        return [permissions.IsAuthenticated()]

    @action(detail=False, methods=["get"])
    def me(self, request) -> Response:
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
