
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from patients.models import PatientProfile

class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
class PatientLoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120)

class PatientProfileForm(ModelForm):
    class Meta:
        model=PatientProfile
        fields="__all__"
        widgets = {
            "user": forms.TextInput(attrs={'class': 'form-control'}),
            "age": forms.TextInput(attrs={'class': 'form-control'}),
            "bloodgroup": forms.TextInput(attrs={'class': 'form-control'}),
            "address": forms.Textarea(attrs={'class': 'form-control'}),
            "phonenumber": forms.TextInput(attrs={'class': 'form-control'}),
        }






