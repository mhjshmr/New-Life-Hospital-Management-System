from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Department

# Create your views here.
class DepartmentListView(ListView):
    model = Department
    template_name = "department/department_list.html"

class DepartmentDetailView(DetailView):
    model = Department
    template_name = "department/department_detail.html"

    # def get_queryset(self):
    #     return super().get_queryset()
