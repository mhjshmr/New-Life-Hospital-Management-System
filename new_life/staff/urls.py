from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path("home", views.home, name="home"),
    path("create", views.create, name="create"),
    path("<int:pk>", views.StaffDetailView.as_view(), name='detail')
]
