from django.contrib import admin
from .models import Humidity, Locations, Name, Temperature, Wind

admin.site.register(Temperature)
admin.site.register(Locations)
admin.site.register(Humidity)
admin.site.register(Name)
admin.site.register(Wind)

# Register your models here.
