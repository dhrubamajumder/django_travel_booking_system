
from django.contrib import admin
from django.urls import path
from . views import home, slide, first, second, third, forms, travel_card, booking_form , booking_forms

urlpatterns = [
    path('home/', home, name='home'),
    path('slide/', slide , name='slide'),
    path('first/', first, name='first'),
    path('second/', second, name='second'),
    path('third/', third, name='third'),

    path('forms/', forms, name='forms'),
    path('booking_forms/', booking_forms, name='booking_forms'),
    path('', travel_card, name='travel_card'),
    path('booking/', booking_form, name='booking_form'),
]