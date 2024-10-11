from rest_framework import serializers

from store.models import Topic, Form


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("id", "name")


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ("id", "name")
