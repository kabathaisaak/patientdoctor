from .models import Doctor
from .forms import DoctorRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import DoctorLoginForm


def get_available_doctors():
    # This function retrieves available doctors from the database
    return Doctor.objects.all()  # You might need to filter this queryset based on availability


def populate_doctors_choices(form):
    form.fields['doctor'].queryset = get_available_doctors()


def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('doctor_dashboard')
    else:
        form = DoctorLoginForm()
    return render(request, 'doctor/doctor_login.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('doctor_login')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor/doctor_register.html', {'form': form})


def doctor_detail(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'doctor/doctor_detail.html', {'doctor': doctor})
