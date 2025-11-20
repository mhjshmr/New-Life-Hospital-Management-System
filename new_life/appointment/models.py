from django.db import models
from django.utils import timezone

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey('patient.Patient', models.CASCADE, blank=True)
    doctor = models.ForeignKey('doctor.Doctor', models.CASCADE)
    issued_staff = models.ForeignKey('staff.Staff', models.CASCADE, blank=True, null=True)
    date_time_of_appointment = models.DateTimeField(default=timezone.now)
    reason = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f'{self.doctor} at {timezone.localtime(self.date_time_of_appointment).strftime("%d-%m-%y %H:%M")}'