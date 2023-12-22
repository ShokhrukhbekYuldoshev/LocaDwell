from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as JwtTokenObtainPairSerializer,
)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token
