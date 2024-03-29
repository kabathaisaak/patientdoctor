from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Doctor



class AppointmentForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=True)
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Select Doctor", required=True)


class DoctorLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


class DoctorRegistrationForm(UserCreationForm):
    specialization = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'specialization']
