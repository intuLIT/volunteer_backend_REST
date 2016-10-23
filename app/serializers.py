from rest_framework import serializers
from app.models import *

# Model Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone', 'location',)

# Serializers
class EmailSerialzer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
