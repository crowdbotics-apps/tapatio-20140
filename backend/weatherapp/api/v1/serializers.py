from rest_framework import serializers
from weatherapp.models import Humidity, Locations, Name, Temperature, Wind


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = "__all__"


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = "__all__"


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = "__all__"


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = "__all__"


class WindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wind
        fields = "__all__"
