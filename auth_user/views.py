from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            if user.user_type == 'admin':
                return redirect('auth_user:admin_dashboard')
            elif user.user_type == 'teacher':
                return HttpResponse('Teacher Dashboard')
            elif user.user_type == 'student':
                return HttpResponse('Student Dashboard')
            else:
                return redirect('auth_user:admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
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


def teacher_dashboard_view(request):
    return render(request, 'auth/teacher_dashboard.html')


def student_dashboard_view(request):
    return render(request, 'auth/student_dashboard.html')
