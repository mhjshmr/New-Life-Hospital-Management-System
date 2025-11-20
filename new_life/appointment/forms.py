from django import forms
from . models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ['date_time_of_appointment']