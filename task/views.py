from rest_framework import viewsets

from .models import Category, DailyTask
from .serializer import CategorySerializer, DailyTaskSerializer


# Create your views here.
class DailyTaskViewSet(viewsets.ModelViewSet):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
