# admin.py
from django.contrib import admin
from .models import Destination

# @admin.register(Destination)
# class DestinationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'seats')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seats', 'days', 'travel_date')
    search_fields = ('name',)
    list_filter = ('travel_date',)