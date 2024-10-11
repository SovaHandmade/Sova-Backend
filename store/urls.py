from django.urls import path, include
from rest_framework import routers

from store.views import ProductViewSet

router = routers.DefaultRouter()
router.register("product", ProductViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "product"
