from rest_framework import authentication
from weatherapp.models import Humidity, Locations, Name, Temperature, Wind
from .serializers import (
    HumiditySerializer,
    LocationsSerializer,
    NameSerializer,
    TemperatureSerializer,
    WindSerializer,
)
from rest_framework import viewsets


class TemperatureViewSet(viewsets.ModelViewSet):
    serializer_class = TemperatureSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Temperature.objects.all()


class LocationsViewSet(viewsets.ModelViewSet):
    serializer_class = LocationsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Locations.objects.all()


class HumidityViewSet(viewsets.ModelViewSet):
    serializer_class = HumiditySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Humidity.objects.all()


class NameViewSet(viewsets.ModelViewSet):
    serializer_class = NameSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Name.objects.all()


class WindViewSet(viewsets.ModelViewSet):
    serializer_class = WindSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Wind.objects.all()
