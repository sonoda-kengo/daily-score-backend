from django.conf.urls import include
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "apiv1"


urlpatterns = [
    path("", include("task.urls")),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
