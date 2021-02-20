from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )


class HomePage(models.Model):
    body = models.TextField()
