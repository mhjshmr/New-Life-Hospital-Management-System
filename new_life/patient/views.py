from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from . import models
from . forms import PatientForm, PatientUpdateForm
from user_profile.forms import UserForm
from new_life.constants import BLOOD_GROUPS, GENDER_CHOICES
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from new_life.constants import SIGN_UP_LAYOUT

# Create your views here.
def home(request):
    return render(request, "index.html", {'name': "Nihaal"})

class PatientListView(ListView):
    template_name = "patient/portfolio.html"
    model = models.Patient

def create(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    pat_form = PatientForm()
    user_form = UserForm()
    error = ""
    
    print(request.method)
    if request.method == 'POST':
        data = request.POST
        user_form = UserForm(data, request.FILES)
        if user_form.is_valid():
            pw, rep_pw = user_form.cleaned_data['password'], user_form.cleaned_data['repeat_password']
            if pw == rep_pw:
                user = user_form.save(commit=False)
                user.set_password(pw)
                user.save()
                
                pat_form = PatientForm({'user': user})
                pat_form.save()

                return redirect('login')
            else:
                error = "Make sure to enter the same password"
        else:
            error = user_form.errors

        messages.add_message(request, messages.ERROR, error)

    return render(request, 'patient/trial_form.html', {'form': user_form, 'genders': GENDER_CHOICES, 'blood_groups': BLOOD_GROUPS, "error": error, 'layout': SIGN_UP_LAYOUT})
    
def home(request):
    return render(request, 'index.html', {'name': 'Nihaal'})

class PatientDetailView(UserPassesTestMixin, DetailView):
    model = models.Patient
    template_name = "patient/patient_detail.html"

    def test_func(self):
        if self.request.user.is_staff or (self.request.user == self.get_object().user):
            return True
        return False
    
def update(request, pk):
    patient = models.Patient.objects.get(pk=pk)
    if request.user != patient.user:
        return redirect('index')
    form = PatientUpdateForm()
    error = ""
    print(request.method)
    
    if request.method == 'POST':
        data = request.POST.copy()
        form = PatientUpdateForm(data, request.FILES, instance=patient)
        # print(data)
        username = data['user_name']
        not_created = User.objects.filter(username=username).exists()
        # print(not_created)
        user = User.objects.get(id=patient.user.id)
        if not not_created:
            user = User.objects.get(username=patient.user.username)
            user.username = username
            user.save()
        else:
            if not username == patient.user.username:
                error = "Username already exists"
        
        pw, rep_pw = data['password'], data['repeat_password']
        if pw:
            if pw == rep_pw:
                user = User.objects.get(id=patient.user.id)
                user.set_password(pw)
            else:
                error = "Make sure to enter the same password"
        if form.is_valid():
            form.save()
            return redirect('patient:detail', pk=pk)
        else:
            error = form.errors

    #     pw, rep_pw = data['password'], data['repeat_password']
    #     if pw == rep_pw:
            # user, not_created = User.objects.get_or_create(username=username)
    #         if form.is_valid():
    #             if not_created:
    #                 user.set_password(pw)
                
    #                 patient = form.save(commit=False)
    #                 patient.user = user

    #                 patient.save()
    #                 user.save()
    #                 return redirect('patient:home')
                    
    #             else:
    #                 error = 'User already exists'

    #         else:
    #             error = form.errors
        
    #     else:
    #         error = "Make sure to enter the same password"

    return render(request, 'patient/update_form.html', {'form': form, 'genders': GENDER_CHOICES, 'blood_groups': BLOOD_GROUPS, "error": error, "patient": patient})

class PatientDeleteView(UserPassesTestMixin,DeleteView):
    model = models.Patient
    template_name = "patient/patient_delete.html"
    
    def get_success_url(self) -> str:
        return reverse_lazy('login')

    def form_valid(self, form):
        print('heloo???')
        patient = models.Patient.objects.get(pk=self.kwargs.get('pk'))
        patient.user.delete()
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff or (self.request.user == self.get_object().user):
            return True
        return False