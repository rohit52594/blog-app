from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import RegisterData
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    
    context = {
        "form": RegisterForm
    }
    return render(request, 'register.html', context)

def userRegister(request):

    form = RegisterForm(request.POST)

    if form.is_valid():

        registerSave = RegisterData(

            name = form.cleaned_data['name'],

            email = form.cleaned_data['email'],

            phone = form.cleaned_data['phone'],

            password = form.cleaned_data['password']

        )

        registerSave.save()

        messages.add_message(request, messages.SUCCESS, 'Registration success')

    return redirect('register')






def privacy(request):
    return render(request, 'privacy-policy.html')
