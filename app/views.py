from app.models import User
from app.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserDetail(APIView):
    def post(self, request, format=None):
        serializer = EmailSerialzer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.data['email'])
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


