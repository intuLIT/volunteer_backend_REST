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

class EventsNearbyList(APIView):
    def post(self, request, format=None):
        serializer = ZipSerializer(data=request.data)
        if serializer.is_valid():
            events = Event.objects.filter(location=serializer.data['zip_code'])
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreateEvent(APIView):
#     def post(self, request, format=None):
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             data = serializer.data
#             serializer = NonProfitSerializer(data['organization'])
#             if serializer.is_valid():
#                 nonprofit = NonProfit.objects.get(pk=0)
#                 print("here")
#                 print(non)
#                 event = Event(name=data['name'],
#                     start_date=data['name'],
#                     end_date=data['end_date'],
#                     address=data['address'],
#                     location=data['location'],
#                     description=data['description'],
#                     photo=data['photo'],
#                     min_volunteers=data['min_volunteers'],
#                     max_volunteers=data['max_volunteers'], 
#                     organization=nonprofit)
#                 goal.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
