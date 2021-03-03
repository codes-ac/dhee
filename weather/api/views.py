import requests
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from weather.serializers import LocationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import authentication, permissions


class WeatherApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer

    def post(self, request):
        print("body--", request.data)
        try:
            if "location" in request.data:
                serializer = self.serializer_class(data = request.data)
                if serializer.is_valid():
                    location = request.data.get('location')
                    url = "http://api.openweathermap.org/data/2.5/weather?q=" + location +"&appid=ddff737555fe75aaf6f86bc5077a1913"
                    response = requests.post(url)
                    for dic in response.json()['weather']:
                        description = dic['description']

            result = {
                "success": True,
                "result": {
                    "description": description,

                },
                # resetList : [ slotTenName, slotElevenName],
                "errorMessageKey": "someMltName"
            }
            return Response(result)

        except:
            return Response({"success": False, "result": "", "errorMessageKey": "Error occured"})
