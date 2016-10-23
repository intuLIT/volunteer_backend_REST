from rest_framework import serializers
from app.models import *

# Model Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone', 'location',)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'start_date', 'end_date',
            'address', 'location', 'description', 'photo',
            'min_volunteers', 'max_volunteers', 'organization')

class NonProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonProfit
        fileds = ('id', 'name', 'description', 'user', 'location')

# Serializers
class EmailSerialzer(serializers.Serializer):
    email = serializers.CharField(max_length=100)