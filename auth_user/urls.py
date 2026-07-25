from django.urls import path
from . import views

app_name = 'auth_user'

urlpatterns = [
    path('', views.login_view, name='login'),
    
]
