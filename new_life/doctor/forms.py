from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Doctor

class DoctorForm(forms.ModelForm):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Doctor
        # fields = '__all__'
        exclude = ["user", "registration_date_time"]
            