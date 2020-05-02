from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


def index(request):
    return render(request, 'solarpv/index.html')


def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                return redirect('/admin/')
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'solarpv/login.html', {'form': form})


def portal(request):
    return render(request, 'solarpv/portal.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'solarpv/register.html', {'form': form})


def certification(request):
    return render(request, 'solarpv/certification.html')
