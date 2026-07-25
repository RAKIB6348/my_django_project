from django.urls import path
from . import views

app_name = 'auth_user'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard_view, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard_view, name='student_dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('logout/', views.logout_view, name='logout'),
]
