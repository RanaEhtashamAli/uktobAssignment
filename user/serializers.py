from django.contrib.auth.models import User
from rest_framework import serializers


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
        )
