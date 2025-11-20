from django.contrib import admin
from .models import Doctor
from .forms import DoctorForm

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    form = DoctorForm
admin.site.register(Doctor)