from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Category, DailyTask


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user_id"] = self.user.id
        data["user_name"] = self.user.username

        return data


class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DailyTask


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category
