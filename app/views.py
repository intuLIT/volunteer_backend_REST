from app.models import User
from app.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from itertools import chain
import json
import requests


class UserDetail(APIView):
    def post(self, request, format=None):
        serializer = EmailSerialzer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.data['email'])
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateEvent(APIView):
    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventsAll(APIView):
    def get(self, request, format=None):
        events = Event.objects.all();
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EventsNearbyList(APIView):
    def post(self, request, format=None):
        serializer = ZipSerializer(data=request.data)
        if serializer.is_valid():
            zip_code = str(serializer.data['zip_code'])
            api_key = 'Mx6es2V0ZQdjuGaR6Rxif5cHnLiel2K7ARl3Tg3T6hcBXnt4e0mu6yctkuIFxtM7'
            r = requests.get('https://www.zipcodeapi.com/rest/'+api_key+'/radius.json/'+zip_code+'/15/mile')

            pjson = json.loads(r.content)

            zip_codes = []
            for location in pjson['zip_codes']:
                zip_codes.append(int(location['zip_code']))
            events = []
            for code in zip_codes:
                events.append(Event.objects.filter(location=code))

            result_list = chain.from_iterable(events)
            serializer = EventSerializer(result_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignUp(APIView):
    def post(self, request, format=None):
        serializer = EventUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
