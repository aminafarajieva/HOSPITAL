from django.shortcuts import render,redirect
from .models import *
from .forms import *
from random import randrange
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django import forms
from django.db.models import Count

# Create your views here.
def main(request):
    h = Hospital.objects.all()
    context = {
        'h': h,
   	}
    return render(request,template_name='HospitalApp/main.html', context=context)

def detail(request, pk):
    one = Hospital.objects.get(pk=pk)
    d = Doctor.objects.filter(hospitals=pk)
    count = Patients.objects.filter(doctor=pk)
    context = {
        'one':one,
        'd':d,
        'count':count, 
    }
    return render(request, 'HospitalApp/index.html', context=context)

class AddPatients(CreateView):
    form_class = AddPatient
    template_name = 'HospitalApp/addnew.html'
    raise_exception = True
    
class AddNurses(CreateView):
    form_class = AddNurse
    template_name = 'HospitalApp/addnew.html'
    raise_exception = True

class AddDoctors(CreateView):
    form_class = AddDoctor
    template_name = 'HospitalApp/addnew.html'
    raise_exception = True

class AddMaindoctors(CreateView):
    form_class = AddMaindoctor
    template_name = 'HospitalApp/addnew.html'
    raise_exception = True

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = UserCreationForm()
    return render(request,'HospitalApp/register.html',{'form':form})

def sigin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('main')         
    else:
        form = AuthenticationForm()
    return render(request,'HospitalApp/login.html',{'form':form})

def signout(request):
    logout(request)
    return redirect('main')



