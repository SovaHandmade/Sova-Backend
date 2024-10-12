from django.urls import path, include
from rest_framework import routers

from store.views import ProductViewSet, FormViewSet, TopicViewSet

router = routers.DefaultRouter()
router.register("product", ProductViewSet)
router.register("form", FormViewSet)
router.register("topic", TopicViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "store"
