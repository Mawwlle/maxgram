from django.urls import include, path
from rest_framework import routers

from car.views import CarConfigurationOrderViewSet, CarConfigurationViewSet, CarViewSet, PurchaseViewSet

router = routers.DefaultRouter()

router.register(r"cars", CarViewSet)
router.register(r"configurations", CarConfigurationViewSet)
router.register(r"orders", CarConfigurationOrderViewSet)
router.register(r"purchases", PurchaseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
