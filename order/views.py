from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer


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


class OrderItemViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = OrderItem.objects.select_related("items")
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)
