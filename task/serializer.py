from rest_framework import serializers

from .models import Category, DailyTask


class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DailyTask


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category
