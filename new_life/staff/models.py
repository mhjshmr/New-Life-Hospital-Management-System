from django.db import models
from new_life.constants import WORKING_HOURS

# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField('user_profile.UserProfile', models.CASCADE)
    department = models.ForeignKey('department.Department', models.CASCADE)
    working_hours = models.CharField(choices=WORKING_HOURS, max_length=11)
    role = models.ForeignKey('staff.Role', models.CASCADE)

    def __str__(self) -> str:
        return self.user.full_name

class Role(models.Model):
    name = models.CharField(max_length=25)
    number_of_staff = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.name