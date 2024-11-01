from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        user = self.request.user

        if user.is_staff:
            return queryset

        return queryset.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
