from django.conf import settings
from django.db import models


class Temperature(models.Model):
    "Generated Model"
    minimum = models.CharField(
        max_length=256,
    )
    maximum = models.CharField(
        max_length=256,
    )


class Locations(models.Model):
    "Generated Model"
    humidity = models.ForeignKey(
        "weatherapp.Humidity",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="locations_humidity",
    )
    temperature = models.ForeignKey(
        "weatherapp.Temperature",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="locations_temperature",
    )
    wind = models.ForeignKey(
        "weatherapp.Wind",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="locations_wind",
    )
    name = models.ForeignKey(
        "weatherapp.Name",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="locations_name",
    )


class Humidity(models.Model):
    "Generated Model"
    humidity = models.CharField(
        max_length=256,
    )


class Name(models.Model):
    "Generated Model"
    city = models.CharField(
        max_length=256,
    )
    state = models.CharField(
        max_length=2,
    )
    latitude = models.CharField(
        max_length=256,
    )
    longitude = models.CharField(
        max_length=256,
    )


class Wind(models.Model):
    "Generated Model"
    wind_speed = models.CharField(
        max_length=256,
    )


# Create your models here.
