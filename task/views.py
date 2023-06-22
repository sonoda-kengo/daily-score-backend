from rest_framework import viewsets

from .models import DailyTask
from .serializer import DailyTaskSerializer


# Create your views here.
class DailyTaskViewSet(viewsets.ModelViewSet):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer
