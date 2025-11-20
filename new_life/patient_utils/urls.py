from django.urls import path
from . import views

app_name = 'utils'
urlpatterns = [
    path("prescription", views.create_prescription, name="prescription"),
    path("", views.MedicalReportListView.as_view(), name="medical_list"),

    path("ajax/load_appointments", views.load_appointments, name="ajax_load"),
]
