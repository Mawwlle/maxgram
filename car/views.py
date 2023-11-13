from rest_framework import permissions, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from car.models import Car, CarConfiguration, CarConfigurationOrder, Purchase
from car.serializers import (
    CarConfigurationOrderSerializer,
    CarConfigurationSerializer,
    CarSerializer,
    PurchaseSerializer,
)
from user.permissions import IsOwnerOrAdmin


class CarConfigurationViewSet(viewsets.ModelViewSet):
    serializer_class = CarConfigurationSerializer
    queryset = CarConfiguration.objects.all()

    def get_permissions(self) -> list[permissions.BasePermission]:
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]

        return [permissions.IsAuthenticated()]


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get_permissions(self) -> list[permissions.BasePermission]:
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]

        return [permissions.IsAuthenticated()]


class CarConfigurationOrderViewSet(viewsets.ModelViewSet):
    serializer_class = CarConfigurationOrderSerializer
    queryset = CarConfigurationOrder.objects.all()

    def get_queryset(self):
        return CarConfigurationOrder.objects.filter(user=self.request.user).order_by("-id")

    def create(self, request: Request, *args, **kwargs):
        serializer = CarConfigurationOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        params = serializer.data.copy()
        configuration_id = params.pop("configuration")
        configuration = get_object_or_404(CarConfiguration, id=configuration_id)

        car_order = CarConfigurationOrder.objects.create(configuration=configuration, user=request.user, **params)
        resp = CarConfigurationOrderSerializer(car_order)

        return Response(resp.data, status=status.HTTP_201_CREATED)

    def get_permissions(self) -> list[permissions.BasePermission]:
        if self.action == "create":
            return []
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]

        return [permissions.IsAuthenticated()]


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all().order_by("-id")
