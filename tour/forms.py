from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'address', 'phone', 'destination', 'guest', 'price']
        widgets = {
            'destination': forms.TextInput(attrs={'id':'destination'}),
            'price': forms.NumberInput(attrs={'id':'price'}),
            'guest': forms.NumberInput(attrs={'id':'guest','min':1,'value':1})
        }
