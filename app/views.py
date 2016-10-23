from app.models import User
from app.serializers import *
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.fpauth import *

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

class ConvertId(APIView):
    def post(self, request, format=None):
        serializer = ConvertIdSerializer(data=request.data)
        if serializer.is_valid():
            np = NonProfit.objects.get(id=serializer.data['id'])
            serializer = NonProfitSerializer(np)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConvertEventId(APIView):
    def post(self, request, format=None):
        serializer = ConvertEventIdSerializer(data=request.data)
        if serializer.is_valid():
            event = Event.objects.get(id=serializer.data['id'])
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventNumSignUps(APIView):
    def post(self, request, format=None):
        serializer = EventIdSerializer(data=request.data)
        if serializer.is_valid():
            e_id = serializer.data['event_id']
            users = EventXUser.objects.filter(eId=e_id)
            total = len(users)
            return JsonResponse({'total':total})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class FacebookLogin(APIView):
#     def post(self, request, format=None):
#         serializer = FacebookAuthSerializer(data=request.data)
#         if serializer.is_valid():
#             app_id = serializer.data['a_id']
#             app_secret = serializer.data['a_secret']

#             GRAPH_API_AUTH_URI = ('https://graph.facebook.com/v2.8/oauth/' 
#                 + 'access_token?'
#                 + 'client_id=' + app_id
#                 + '&redirect_uri=' + 'http://54.153.15.7:8080/'
#                 + '&client_secret=' + self.app_secret
#                 + '&code=')
#             r = requests.get(GRAPH_API_AUTH_URI)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)