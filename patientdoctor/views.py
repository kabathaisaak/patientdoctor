from django.shortcuts import render





def login_interface(request):
    return render(request, 'login_interface.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def doctor_dashboard(request):
    return render(request,'doctor_dashboard.html')


def patient_dashboard(request):
    return render(request,'patient_dashboard.html')