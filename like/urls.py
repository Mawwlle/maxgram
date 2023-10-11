from django.urls import include, path
from rest_framework import routers

from like.views import LikeViewSet

router = routers.DefaultRouter()
router.register(r"likes", LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
