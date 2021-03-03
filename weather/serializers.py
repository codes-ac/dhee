from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    cityname = serializers.CharField(max_length=15)

