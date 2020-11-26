from django.contrib.auth import authenticate,logout,login
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from patients.forms import PatientRegistrationForm,PatientLoginForm,PatientProfileForm
from django.contrib.auth.decorators import login_required

from patients.models import PatientProfile
# Create your views here.

def patientRegistration(request):
    form=PatientRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("psignin")
        else:
            context["form"] = form
            return render(request,"patients/patregistration.html",context)
    return render(request, "patients/patregistration.html", context)

def signIn(request):
    form=PatientLoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=PatientLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if(user):
                login(request,user)
                return redirect("phome")
            else:
                context["form"] = form
                return render(request,"patients/patlogin.html", context)

    return render(request,"patients/patlogin.html", context)

def logOut(request):
    logout(request)
    return redirect("psignin")

@login_required(login_url="psignin")

def patientHome(request):

    return render(request,"patients/phome.html")

@login_required(login_url="psignin")

def createProfile(request):

    form=PatientProfileForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=PatientLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("phome")
        else:
            context["form"] = form

    # return render(request,"patients/pprofile.html",context)






