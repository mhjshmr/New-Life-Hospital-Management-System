from django.urls import path
from . import views

app_name = 'patient'
urlpatterns = [
    path("home", views.home, name="home"),
    path("create", views.create, name="create"),
    path("<int:pk>", views.PatientDetailView.as_view(), name="detail"),
    path("update/<int:pk>", views.update, name="update"),
    path("delete/<int:pk>", views.PatientDeleteView.as_view(), name="delete"),
    
]
