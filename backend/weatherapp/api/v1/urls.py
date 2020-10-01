from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CloudinessViewSet,
    HumidityViewSet,
    LocationsViewSet,
    NameViewSet,
    TemperatureViewSet,
    WindViewSet,
)

router = DefaultRouter()
router.register("temperature", TemperatureViewSet)
router.register("locations", LocationsViewSet)
router.register("humidity", HumidityViewSet)
router.register("name", NameViewSet)
router.register("wind", WindViewSet)
router.register("cloudiness", CloudinessViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
