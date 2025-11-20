from django import forms
from . models import Staff

class StaffForm(forms.ModelForm):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Staff
        # fields = '__all__'
        exclude = ["user", "registration_date_time"]
            