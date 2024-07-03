from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from app.forms1 import LoginForm, RegisterModelForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})



def logout_page(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')
    return render(request, 'auth/logout.html')

def register_page(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            login(request, user)
            return redirect('index')
    else:
        form = RegisterModelForm()

    return render(request, 'auth/register.html', {'form': form})
