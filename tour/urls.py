
from django.contrib import admin
from django.urls import path
from . views import home, slide, first, second, third, travel_card, booking_form , booked_list, booking_forms, form_booking, create_blog, blog_list, blog_detail, delete_blog
urlpatterns = [
    path('home/', home, name='home'),
    path('slide/', slide , name='slide'),
    path('first/', first, name='first'),
    
    path('blog_urls/', second, name='second'),
    path('third/', third, name='third'),

    path('', travel_card, name='travel_card'),
    path('booking/', booking_form, name='booking_form'),

    path('bookings/', booking_forms, name='forms'),
    path('booked/', booked_list, name='booked_list'),
    path('forms/<int:id>/', form_booking, name='form_booking'),

    # path('new_blog/', blog_form, name="blog_form"),
    path('create/', create_blog, name='create_blog'),
    path('blog_list', blog_list, name='blog_list'),
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),
]