from django.urls import path
from . import views


urlpatterns = [
    path('<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('login/', views.doctor_login, name='doctor_login'),
    path('register/', views.doctor_register, name='doctor_register'),

]

