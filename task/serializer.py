from rest_framework import serializers

from .models import DailyTask


class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DailyTask
