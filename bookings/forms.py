from django import forms

from bookings.models import booking


class bookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['occupant', 'room_number','roll_number', 'occupied']