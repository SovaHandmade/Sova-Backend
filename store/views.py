from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from store.models import Topic
from store.permissions import IsAdminOrReadOnly
from store.serializers import TopicSerializer


class TopicViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAdminOrReadOnly,)
