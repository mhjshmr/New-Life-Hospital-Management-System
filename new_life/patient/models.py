from django.db import models

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField('user_profile.UserProfile', models.CASCADE, blank=True)
    
    def __str__(self) -> str:
        return self.user.full_name