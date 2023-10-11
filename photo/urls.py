from django.urls import include, path
from rest_framework import routers

from photo.views import PhotoViewSet

router = routers.DefaultRouter()
router.register(r"photos", PhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
