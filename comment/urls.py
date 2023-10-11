from django.urls import include, path
from rest_framework import routers

from comment.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
