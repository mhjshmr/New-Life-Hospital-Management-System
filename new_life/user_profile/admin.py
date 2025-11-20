from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(UserAdmin):
    req_fields = list(UserAdmin.fieldsets)
    req_fields[1] = (
        'Personal Info', {
            'fields': ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'gender', 'blood_group', 'address']
        }
    )
    UserAdmin.fieldsets = req_fields
    
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Info', {
                'fields': ['eid', 'category', 'profile_pic']
            }
        )

    )

admin.site.register(UserProfile, UserProfileAdmin)
