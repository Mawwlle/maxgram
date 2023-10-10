from typing import Any

from rest_framework import viewsets


class GenericViewSet(viewsets.GenericViewSet):
    serializer_action_classes: dict[str, Any] | None = None

    def get_serializer_class(self) -> Any | None:
        action_classes = self.serializer_action_classes

        return action_classes.get(self.action) if action_classes else super().get_serializer_class()
