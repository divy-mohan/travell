# booking/forms.py

from django import forms
from .models import Booking, HotelBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'preferred_date': forms.SelectDateWidget(),
            'alternative_dates': forms.Textarea(attrs={'rows': 2}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
            'accommodation_preferences': forms.Textarea(attrs={'rows': 3}),
        }
        
class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = ['name', 'email', 'phone', 'check_in_date', 'check_out_date', 'guests', 'special_requests']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }

