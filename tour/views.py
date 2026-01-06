from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Destination

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

def forms(request):
    return render(request, 'form.html')

def booking_forms(request):
    return render(request, 'booking_form.html')



def booking_form(request):
    destination_id = request.GET.get('id')
    destination = get_object_or_404(Destination, id=destination_id)

    if request.method == 'POST':
        guest = int(request.POST['guest'])

        if guest > destination.seats:
            return render(request, 'form.html', {
                'destination': destination,
                'error': 'Not enough seats available'
            })

        destination.seats -= guest
        destination.save()
        return redirect('success')

    return render(request, 'form.html', {
        'destination': destination
    })




# def travel_card(request):
#     destination = Destination.objects.all()
#     return render(request, 'blog.html', { 'destination': destination })

def travel_card(request):
    destination = Destination.objects.all()
    return render(request, 'blog.html', {'destination': destination})