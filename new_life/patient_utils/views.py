from django.shortcuts import render, redirect
from doctor.models import Doctor
from patient.models import Patient
from appointment.models import Appointment
from . forms import PrescriptionForm
from . models import MedicalReport
from django.views.generic import ListView

# Create your views here.
def create_prescription(request):
    if not request.user.is_staff:
        return redirect('index')
    doctor = Doctor.objects.get(user=request.user)
    patients = Appointment.objects.filter(doctor=doctor)
    apts = Appointment.objects.none()

    if request.method == 'POST':
        form = PrescriptionForm(request.POST)

        if form.is_valid():
            presc = form.save(commit=False)
            presc.doctor = doctor
            presc.save()
            med_report = MedicalReport.objects.create(patient=presc.patient, prescription=presc)
            med_report.save()
    return render(request, 'patient_utils/prescription_form.html', {'patients': patients, 'apts': apts})

def load_appointments(request):
    patient_id = request.GET.get('patient_id')
    patient = Patient.objects.get(pk=patient_id)
    doctor = Doctor.objects.get(user=request.user)

    apts = Appointment.objects.filter(doctor=doctor, patient=patient)

    return render(request, 'patient_utils/render_appointments.html', {'apts': apts})

class MedicalReportListView(ListView):
    model = MedicalReport
    template_name = "patient_utils/medical_list.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return redirect('index')
        return super().get(request, *args, **kwargs)