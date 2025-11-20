from django.db import models
from new_life.constants import WORKING_HOURS

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField('user_profile.UserProfile', models.CASCADE)
    department = models.ForeignKey('department.Department', models.CASCADE)
    working_hours = models.CharField(choices=WORKING_HOURS, max_length=11)
    room = models.CharField(blank=False, max_length=10)
    # appointments = models.ForeignKey('appointment.Appointment', models.CASCADE, related_name='doc_appointments', blank=True)
    
    def __str__(self) -> str:
        return self.user.full_name
