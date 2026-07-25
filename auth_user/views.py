from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('auth_user:admin_dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'auth/login.html')


def admin_dashboard_view(request):
    return render(request, 'auth/admin_dashboard.html')


def profile_view(request):
    return render(request, 'auth/profile.html')


def profile_edit_view(request):
    return render(request, 'auth/profile_edit.html')


def logout_view(request):
    logout(request)
    return redirect('auth_user:login')
