from django.urls import path, include
from rest_framework import routers

from store.views import ProductViewSet, CombinedViewSet

router = routers.DefaultRouter()
router.register("product", ProductViewSet)
router.register("tags", CombinedViewSet, basename="combined")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]

app_name = "store"
