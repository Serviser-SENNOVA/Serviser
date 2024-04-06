from rest_framework import serializers
from .models import User


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # or ( field, field )
        fields = '__all__'
