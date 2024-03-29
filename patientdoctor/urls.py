from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_interface, name='login interface'),
    path('about', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    ]

