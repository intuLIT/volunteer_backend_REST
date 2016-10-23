from rest_framework import serializers, relations
from app.models import *


# Model Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone', 'location', 'organization', 'picture')

class NonProfitSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = NonProfit
        fields = ('id', 'name', 'description', 'user', 'location', 'picture')

class EventSerializer(serializers.ModelSerializer):
    organization = relations.PrimaryKeyRelatedField(queryset=NonProfit.objects.all())
    class Meta:
        model = Event
        fields = ('id', 'name', 'start_date', 'end_date',
            'address', 'location', 'description', 'photo',
            'min_volunteers', 'max_volunteers', 'organization')

class EventUserSerializer(serializers.ModelSerializer):
    uId = relations.PrimaryKeyRelatedField(queryset=User.objects.all())
    eId = relations.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = EventXUser
        fields = ('uId', 'eId')

# Serializers
class EmailSerialzer(serializers.Serializer):
    email = serializers.CharField(max_length=100)

class ZipSerializer(serializers.Serializer):
    zip_code = serializers.IntegerField()

class ConvertIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class ConvertEventIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class FacebookAuthSerializer(serializers.Serializer):
    a_id = serializers.CharField(max_length=200)
    a_secret = serializers.CharField(max_length=200)

class EventIdSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()