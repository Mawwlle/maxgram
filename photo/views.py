from django.http import FileResponse
from rest_framework import parsers, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request

from photo.models import Photo
from photo.serializers import PhotoSerializer
from user.models import User


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["created_at", "user"]
    search_fields = ["caption"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ["update", "partial_update", "destroy"]:
            queryset = queryset.filter(user=self.request.user.pk)

        return queryset

    def perform_create(self, serializer: PhotoSerializer) -> None:
        user = get_object_or_404(User, pk=self.request.user.pk)
        serializer.save(user=user)

    def retrieve(self, request: Request, *args, **kwargs) -> FileResponse:
        return FileResponse(self.get_object().image)
