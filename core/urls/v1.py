from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

docs = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
auth = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = [
    path("docs/", include(docs)),
    path("", include(auth)),
    path("", include("user.urls")),
    path("", include("photo.urls")),
    path("", include("comment.urls")),
]
