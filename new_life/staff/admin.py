from django.contrib import admin
from . models import Role, Staff
# Register your models here.
admin.site.register([Role, Staff])