from django.shortcuts import render, redirect
from . forms import StaffForm
from django.contrib.auth.models import User
from new_life.constants import BLOOD_GROUPS, GENDER_CHOICES, WORKING_HOURS
from django.views.generic import DetailView
from . models import Role, Staff
from department.models import Department
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
def create(request):
    if not request.user.is_staff:
        return redirect('index')
    form = StaffForm()
    error = ""
    role = Role.objects.all()
    department = Department.objects.all()

    print(request.method)
    if request.method == 'POST':
        data = request.POST.copy()
        form = StaffForm(data, request.FILES)

        username = data['user_name']
        pw, rep_pw = data['password'], data['repeat_password']
        if pw == rep_pw:
            user, not_created = User.objects.get_or_create(username=username)
            if form.is_valid():
                if not_created:
                    user.set_password(pw)
                    user.is_staff = True
                    
                    staff = form.save(commit=False)
                    staff.user = user

                    staff.save()
                    user.save()

                    return redirect('index')
                else:
                    error = 'User already exists'

            else:
                error = form.errors
        else:
            error = "Make sure to enter the same password"

    return render(request, 'staff/forms.html', {'form': form, 'genders': GENDER_CHOICES, 'blood_groups': BLOOD_GROUPS, "error": error, "roles": role, "departments": department, "working_hours": WORKING_HOURS})
    
def home(request):
    return render(request, 'index.html', {'name': 'Nihaal'})

class StaffDetailView(UserPassesTestMixin, DetailView):
    model = Staff
    template_name = "staff/staff_detail.html"

    def test_func(self):
        return self.request.user.is_staff