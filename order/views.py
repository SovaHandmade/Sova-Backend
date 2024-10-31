from django.db.models import Sum, ExpressionWrapper, F, IntegerField, Prefetch
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from order.models import Order, OrderItem
from order.serializers import OrderSerializer


class ReservationPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Order.objects.annotate(
        total=Sum(
            ExpressionWrapper(
                F("product.price") * F("quantity"), output_field=IntegerField()
            )
        ),
    ).prefetch_related(
        Prefetch(
            "items",
            queryset=OrderItem.objects.annotate(
                total=ExpressionWrapper(
                    F("product.price") * F("quantity"), output_field=IntegerField()
                )
            ),
        )
    )
    serializer_class = OrderSerializer
    pagination_class = ReservationPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
