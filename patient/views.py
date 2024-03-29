from django.shortcuts import render, redirect
from .forms import PatientRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import PatientLoginForm
from .models import Patient
from django.shortcuts import render, redirect
from doctor.forms import AppointmentForm
from doctor.models import Appointment

def view_appointments(request):
    # Fetch appointments for the logged-in patient
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'view_appointments.html', {'appointments': appointments})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.status = 'pending'
            appointment.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')


def patient_detail(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'patient/detail.html', {'patient': patient})



def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            patient = Patient.objects.get(user=user)
            return redirect('patient_dashboard')
    else:
        form = PatientLoginForm()
    return render(request, 'patient/patient_login.html', {'form': form})





def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('patient_login')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient/patient_register.html', {'form': form})
