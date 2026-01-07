from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Destination
from django.contrib import messages
from django.db import transaction


# Create your views here.
def home(request):
    destination = Destination.objects.all()
    return render(request, 'home.html', {'destination': destination})


def slide(request):
    return render(request, 'slid.html')


def first(request):
    return render(request, 'first_blog.html')

def second(request):
    return render(request, 'second_blog.html')

def third(request):
    return render(request, 'third.html')


def booking_form(request):
    destination_id = request.GET.get('id') or request.POST.get('destination')
    if not destination_id:
        return redirect('home')

    destination = get_object_or_404(Destination, id=destination_id)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        try:
            guest = int(request.POST.get('guest', 1))
            price_per_person = float(request.POST.get('price', 0))
        except ValueError:
            guest = 1
            price_per_person = 0

        total_price = guest * price_per_person

        if guest <= 0 or total_price <= 0:
            return render(request, 'form.html', {
                'destination': destination,
                'error': 'Invalid guest number or price'
            })

        with transaction.atomic():
            # Lock the row to avoid race conditions
            destination = Destination.objects.select_for_update().get(id=destination.id)

            if guest > destination.seats:
                return render(request, 'form.html', {
                    'destination': destination,
                    'error': 'Not enough seats available'
                })

            destination.seats -= guest
            destination.save()

            Booking.objects.create(
                full_name=full_name,
                address=address,
                phone=phone,
                destination=destination,
                guest=guest,
                total_price=total_price
            )

        return redirect('home')

    return render(request, 'form.html', {'destination': destination})




def booked_list(request):
    bookings = Booking.objects.order_by('-booked_at')
    return render(request, 'booked_list.html', {'bookings': bookings})


def travel_card(request):
    destination = Destination.objects.all()
    return render(request, 'blog.html', {'destination': destination})


def booking_forms(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        destination_id = request.POST.get('destination')
        guest = int(request.POST.get('guest'))
        price = float(request.POST.get('price'))

        destination = Destination.objects.get(id=destination_id)

        total_price = guest * price

        Booking.objects.create(
            full_name=full_name,
            address=address,
            phone=phone,
            destination=destination,
            guest=guest,
            total_price=total_price
        )

        # ✅ Success message
        messages.success(request, f"Booking successful for {destination.name}!")
        return redirect('home')  # redirect করলে message দেখাবে

    return render(request, 'booking_form.html')



