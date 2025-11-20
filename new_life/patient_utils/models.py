from django.db import models
from django.utils import timezone

# Create your models here.
class Lab(models.Model):
    patient = models.ForeignKey('patient.Patient', models.CASCADE)
    doctor = models.ForeignKey('doctor.Doctor', models.CASCADE)
    staff = models.ForeignKey('staff.Staff', models.CASCADE)
    date_of_release = models.DateField()

    def __str__(self) -> str:
        return f'{self.patient} for {self.doctor}'

class XRay(models.Model):
    patient = models.ForeignKey('patient.Patient', models.CASCADE)
    doctor = models.ForeignKey('doctor.Doctor', models.CASCADE)
    staff = models.ForeignKey('staff.Staff', models.CASCADE)
    date_of_release = models.DateField()

    def __str__(self) -> str:
        return f'{self.patient} for {self.doctor}'

class MedicalReport(models.Model):
    patient = models.ForeignKey('patient.Patient', models.CASCADE)
    lab = models.ForeignKey('patient_utils.Lab', models.CASCADE, null=True, blank=True)
    xray = models.ForeignKey('patient_utils.XRay', models.CASCADE, null=True, blank=True)
    allergies = models.CharField(max_length=25, blank=True, null=True)
    prescription = models.ForeignKey('patient_utils.Prescription', models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.patient.__str__()

    
class Prescription(models.Model):
    doctor = models.ForeignKey('doctor.Doctor', models.CASCADE)
    patient = models.ForeignKey('patient.Patient', models.CASCADE)
    appointment = models.ForeignKey('appointment.Appointment', models.CASCADE)
    medicines = models.CharField(max_length=50)
    instructions = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.doctor} for {self.patient}'
    