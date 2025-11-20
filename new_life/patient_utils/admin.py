from django.contrib import admin
from . models import Lab, XRay, MedicalReport, Prescription
# Register your models here.

admin.site.register([Lab, XRay, MedicalReport, Prescription])