from django.contrib import admin
from .models import Plant

@admin.register(Plant)

class plantAdmin(admin.ModelAdmin):
    list_display = ['name', 'variety', 'type', 'condition', 'location_general', 'location_specific', 'latitude', 'longitude', 'date', 'description']
