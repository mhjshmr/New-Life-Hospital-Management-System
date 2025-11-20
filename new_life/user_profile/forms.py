from django import forms
from .models import UserProfile
from new_life.constants import REGISTRATION_FIELDS, WIDGET_ATTRS

class UserForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Address')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    repeat_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    
    class Meta:
        model = UserProfile
        fields = REGISTRATION_FIELDS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            for wid, attrs in WIDGET_ATTRS.items():
                if isinstance(field, wid):
                    field.widget.attrs.update(attrs)
