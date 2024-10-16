from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from store.models import Topic, Form, Product, Tag
from store.permissions import IsAdminOrReadOnly
from store.serializers import (
    ProductSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    ProductImageSerializer,
    TopicSerializer,
    FormSerializer,
)


class CombinedView(APIView):
    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        forms = Form.objects.all()

        topics_data = TopicSerializer(topics, many=True).data
        forms_data = FormSerializer(forms, many=True).data

        combined_data = {"topics": topics_data, "forms": forms_data}

        return Response(combined_data)


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Product.objects.prefetch_related("form", "topic")
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        form = self.request.query_params.get("form")
        topic = self.request.query_params.get("topic")

        queryset = self.queryset

        if form:
            queryset = queryset.filter(form__name__icontains=form)

        if topic:
            queryset = queryset.filter(topic__name__icontains=topic)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer

        if self.action == "retrieve":
            return ProductDetailSerializer

        if self.action == "upload_image":
            return ProductImageSerializer

        return ProductSerializer

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsAdminUser],
    )
    def upload_image(self, request, pk=None):
        """Endpoint for uploading image to specific movie"""
        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
