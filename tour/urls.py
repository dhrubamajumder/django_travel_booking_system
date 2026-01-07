
from django.contrib import admin
from django.urls import path
from . views import home, slide, first, second, third, travel_card, booking_form , booked_list, booking_forms

urlpatterns = [
    path('home/', home, name='home'),
    path('slide/', slide , name='slide'),
    path('first/', first, name='first'),
    
    path('second/', second, name='second'),
    path('third/', third, name='third'),

    path('', travel_card, name='travel_card'),
    path('booking/', booking_form, name='booking_form'),

    path('bookings/', booking_forms, name='forms'),
    path('booked/', booked_list, name='booked_list'),
]