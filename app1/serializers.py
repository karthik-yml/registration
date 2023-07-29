# serializers.py

from rest_framework import serializers
from .models import EMP

class EMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMP
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Please provide both email and password.")

        return data

