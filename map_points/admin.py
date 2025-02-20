from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.admin import GISModelAdmin
from .models import MapPoints

@admin.register(MapPoints)
class MapPointAdmin(GISModelAdmin):
    list_display = ('title','category')