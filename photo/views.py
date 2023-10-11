from django.http import FileResponse
from drf_spectacular.utils import extend_schema
from rest_framework import parsers, permissions, status, viewsets
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

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.pk)

    def perform_create(self, serializer: PhotoSerializer) -> None:
        user = get_object_or_404(User, pk=self.request.user.pk)
        serializer.save(user=user)

    @extend_schema(responses={status.HTTP_200_OK: FileResponse})
    def retrieve(self, request: Request, *args, **kwargs) -> FileResponse:
        return FileResponse(self.get_object().image)
