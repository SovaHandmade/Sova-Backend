from django.urls import path, include
from rest_framework import routers

from store.views import ProductViewSet, CombinedView

router = routers.DefaultRouter()
router.register("product", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("tags/", CombinedView.as_view(), name="combined-view"),
]

app_name = "store"
