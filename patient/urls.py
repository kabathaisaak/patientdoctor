from django.urls import path
from . import views
from .views import book_appointment, appointment_success,view_appointments


urlpatterns = [
    path('<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('login/', views.patient_login, name='patient_login'),
    path('register/', views.patient_register, name='patient_register'),
    path('<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('book/', book_appointment, name='book_appointment'),
    path('success/', appointment_success, name='appointment_success'),
    path('appointments/', view_appointments, name='view_appointments'),
]
