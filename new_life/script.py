import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_life.settings")

import django
django.setup()

import json
from department.models import Department
from staff.models import Role
from patient.forms import PatientForm
from doctor.forms import DoctorForm
from staff.forms import StaffForm
from user_profile.models import UserProfile
from random import choice

file = open('../data.json','r')

js = json.load(file)

def make_department():
    for department in js['departments'].values():
        dept, not_created = Department.objects.get_or_create(**department)
        if not_created:
            dept.save()

def make_roles():
    for role in js['roles'].values():
        role, not_created = Role.objects.get_or_create(**role)
        if not_created:
            role.save()

def make_patients():
    for patient in js['patients'].values():
        patient['password'] = 'asdasd'
        patient['repeat_password'] = 'asdasd'
        
        form = PatientForm(patient)
        if form.is_valid():
            data = form.cleaned_data
            username = data['user_name']
            password = data['password']

            user, not_created = UserProfile.objects.get_or_create(username=username, password=password, full_name=patient['full_name'], category="P", date_of_birth=patient['date_of_birth'], phone_number=patient['phone_number'], gender=patient['gender'], blood_group=patient['blood_group'], address=patient['address'], eid=patient['eid'])

            if not_created:
                user.set_password(password)

                patient = form.save(commit=False)
                patient.user = user

                patient.save()
                user.save()

def make_doctors():
    for doctor in js['doctors'].values():
        doctor['password'] = 'asdasd'
        doctor['repeat_password'] = 'asdasd'
        
        dept_id = Department.objects.get(name=doctor['department'])
        working_hours = choice(('08:00-13:00', '13:00-18:00', '18:00-00:00'))
        doctor['working_hours'] = working_hours
        doctor['department'] = dept_id

        form = DoctorForm(doctor)

        if form.is_valid():
            data = form.cleaned_data
            username = data['user_name']
            password = data['password']

            user, not_created = UserProfile.objects.get_or_create(username=username, password=password, full_name=doctor['full_name'], category="D", date_of_birth=doctor['date_of_birth'], phone_number=doctor['phone_number'], gender=doctor['gender'], blood_group=doctor['blood_group'], eid=doctor['eid'])

            if not_created:
                user.set_password(password)
                user.is_staff = True

                doctor = form.save(commit=False)
                doctor.user = user

                doctor.save()
                user.save()

def make_staffs():
    for staff in js['staffs'].values():
        staff['password'] = 'asdasd'
        staff['repeat_password'] = 'asdasd'
        
        dept_id = Department.objects.get(name=staff['department'])
        role_id = Role.objects.get(name=staff['role'])
        working_hours = choice(('08:00-13:00', '13:00-18:00', '18:00-00:00'))
        staff['working_hours'] = working_hours
        staff['department'] = dept_id
        staff['role'] = role_id

        form = StaffForm(staff)
        
        if form.is_valid():
            data = form.cleaned_data
            username = data['user_name']
            password = data['password']

            user, not_created = UserProfile.objects.get_or_create(username=username, password=password, full_name=staff['full_name'], category="S", date_of_birth=staff['date_of_birth'], phone_number=staff['phone_number'], gender=staff['gender'], blood_group=staff['blood_group'], eid=staff['eid'])

            if not_created:
                user.set_password(password)
                user.is_staff = True

                staff = form.save(commit=False)
                staff.user = user

                staff.save()
                user.save()

make_department()
make_roles()
make_patients()
make_staffs()
make_doctors()

file.close()