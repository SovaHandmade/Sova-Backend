from django.urls import path, include
from rest_framework import routers

from store.views import ProductViewSet, TagViewSet  # FormViewSet, #TopicViewSet

router = routers.DefaultRouter()
router.register("product", ProductViewSet)
router.register("tag", TagViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "store"
