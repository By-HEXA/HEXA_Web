"""
URL configuration for HEXA_Web_Sign_In project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from Sign_In_app import views
from django.contrib.auth import views as auth_views

app_name = 'Sign_app'

urlpatterns = [
    path('Up', views.SignUp, name='SignUp'),
    path('In', views.SignIn, name='SignIn'),
    path('Out', views.SignOut, name='SignOut'),
    path('Del', views.DeleteAccount, name='DeleteAccount'),
    path('Find_ID', views.Find_ID, name='Find_ID'),
    path('Check_ID', views.Check_ID, name='Check_ID'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
