from rest_framework import serializers
from rest_framework_simplejwt.serializers import (  # TokenRefreshSerializer,
    TokenObtainPairSerializer,
)

from .models import Category, DailyTask


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["expires_in"] = refresh.access_token.lifetime
        user_data = {"id": self.user.id, "name": self.user.username, "email": self.user.email}
        data["user"] = user_data

        return data


class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DailyTask


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category
