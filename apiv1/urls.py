from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from task import views

app_name = "task-api"

router = routers.SimpleRouter()
router.register("tasks", views.DailyTaskViewSet, basename="task")
router.register("categories", views.CategoryViewSet, basename="category")


urlpatterns = [
    path("", include(router.urls)),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
