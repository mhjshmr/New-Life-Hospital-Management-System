from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=25)
    number_of_staffs = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.name