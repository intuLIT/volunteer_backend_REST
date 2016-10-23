from rest_framework import serializers
from snippets.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'name', 'email', 'phone', 'location',)
