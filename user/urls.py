from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import CreateUserView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token-renew/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"