from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from task import views

app_name = "task-api"

router = routers.SimpleRouter()
router.register("tasks", views.DailyTaskViewSet, basename="task")


urlpatterns = [
    path("", include(router.urls)),
]
