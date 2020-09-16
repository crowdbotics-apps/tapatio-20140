from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
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

urlpatterns = [
    path("", include(router.urls)),
]
