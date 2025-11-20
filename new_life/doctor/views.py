from django.shortcuts import render, redirect
from . forms import DoctorForm
from . models import Doctor
from department.models import Department
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.db.models import Count

from new_life.constants import BLOOD_GROUPS, WORKING_HOURS, GENDER_CHOICES

# Create your views here.
def create(request):
    if not request.user.is_staff:
        return redirect('index')
    form = DoctorForm()
    error = ""
    
    print(request.method)
    
    departments = Department.objects.all()
    if request.method == 'POST':
        data = request.POST.copy()
        form = DoctorForm(data, request.FILES)

        username = data['user_name']
        pw, rep_pw = data['password'], data['repeat_password']
        if pw == rep_pw:
            user, not_created = User.objects.get_or_create(username=username)
            if form.is_valid():
                if not_created:
                    user.set_password(pw)
                    user.is_staff = True
                    
                    doctor = form.save(commit=False)
                    doctor.user = user

                    doctor.save()
                    user.save()

                    redirect("index")
                else:
                    error = 'User already exists'

            else:
                error = form.errors
        else:
            error = "Make sure to enter the same password"

    return render(request, 'doctor/forms.html', {'form': form, 'genders': GENDER_CHOICES, 'departments': departments, 'blood_groups': BLOOD_GROUPS, 'working_hours': WORKING_HOURS, "error": error})

# class DoctorView(FormView):
#     template_name = 'forms.html'
#     form_class = DoctorForm
#     success_url = reverse_lazy('doctor:new')

#     def get_context_data(self, val='', **kwargs):
#         print('executing context')
#         departments = Department.objects.all()
#         context = super().get_context_data() | {'genders': GENDER_CHOICES, 'departments': departments, 'blood_groups': BLOOD_GROUPS, 'working_hours': WORKING_HOURS, 'error': val}
#         print(context)
#         return context

#     # def form_valid(self, form):
#     #     data = form.cleaned_data
#     #     print(data)
#     #     username = data['user_name']
#     #     pw, rep_pw = data['password'], data['repeat_password'] 
#     #     if pw == rep_pw:
#     #         user, not_created = User.objects.get_or_create(username=username)
#     #         if not_created:
#     #             user.set_password(pw)
            
#     #             doctor = form.save(commit=False)
#     #             doctor.user = user

#     #             doctor.save()
#     #             user.save()
#     #         else:
#     #             self.errors = 'User already exists'

#     #     else:
#     #         self.errors = "Make sure to enter the same password"

#     #     if self.errors:
#     #         print(self.errors)
#     #         print(self.get_context_data(self.errors))
#     #         self.success_url = reverse('doctor:create')
        
#     #     return super().form_valid(form)

#     def form_invalid(self, form):
#         self.errors = form.errors
#         print(self.get_context_data())
        
#         return super().form_invalid(form)

#     def post(self, request, *args, **kwargs):
#         form = DoctorForm(request.POST, request.FILES)
#         data = form.data
#         print(data)
#         username = data['user_name']
#         pw, rep_pw = data['password'], data['repeat_password'] 
#         if pw == rep_pw:
#             user, not_created = User.objects.get_or_create(username=username)
#             if form.is_valid():
#                 if not_created:
#                     user.set_password(pw)
                
#                     doctor = form.save(commit=False)
#                     doctor.user = user

#                     doctor.save()
#                     user.save()
#                 else:
#                     self.errors = 'User already exists'
#             else:
#                 self.errors = form.errors
#         else:
#             self.errors = "Make sure to enter the same password"

#         if self.errors:
#             print(self.errors)
#             print(self.get_context_data(self.errors))
#             self.success_url = reverse('doctor:create')
#         return super().post(request, *args, **kwargs)
    
def home(request):
    return render(request, 'index.html', {'name': 'Nihaal'})

class DoctorListView(ListView):
    model = Doctor
    template_name = "doctor/doctor_list.html"

    def get_queryset(self):
        query_set = super().get_queryset().order_by('department')
        return query_set

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "doctor/doctor_detail.html"
