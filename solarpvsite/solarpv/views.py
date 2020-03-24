from django.shortcuts import render

def index(request):
    return render(request, 'solarpv/index.html')

def login(request):
    return render(request, 'solarpv/login.html')

def portal(request):
    return render(request, 'solarpv/portal.html')

def register(request):
    return render(request, 'solarpv/register.html')
