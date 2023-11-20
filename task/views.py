from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Category, DailyTask
from .serializer import CategorySerializer, DailyTaskSerializer


class DailyTaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
