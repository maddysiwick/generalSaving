from django.contrib import admin
from .models import Doctor,Language
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
admin.site.register(Language)
admin.site.register(Doctor)
class DoctorAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')