from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from doctor.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']


class PatientRegistrationForm(UserCreationForm):
    age = forms.IntegerField()
    gender = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age', 'gender']


class PatientLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


