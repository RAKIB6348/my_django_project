from django.urls import path
from . import views

app_name = 'auth_user'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('profile/', views.profile_view, name='profile'),
]
