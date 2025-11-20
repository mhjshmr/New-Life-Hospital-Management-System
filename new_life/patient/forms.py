from django import forms
from . models import Patient
from user_profile.models import UserProfile
from new_life.constants import REGISTRATION_FIELDS, WIDGET_ATTRS

class PatientForm(forms.ModelForm):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Patient
        fields = '__all__'
            
class PatientUpdateForm(forms.ModelForm):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    repeat_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    class Meta:
        model = Patient
        # fields = '__all__'
        exclude = ["user", "registration_date_time"]
            

# class PatientForm(forms.ModelForm):
#     address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Address')
#     password = forms.CharField(widget=forms.PasswordInput(), label='Password')
#     repeat_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    
#     class Meta:
#         model = UserProfile
#         # fields = '__all__'
#         fields = REGISTRATION_FIELDS

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             for wid, attrs in WIDGET_ATTRS.items():
#                 if isinstance(field, wid):
#                     field.widget.attrs.update(attrs)
#             print(field, field.label, field.widget)