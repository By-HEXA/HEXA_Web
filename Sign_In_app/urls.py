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

app_name = 'HEXA_Web'

urlpatterns = [
    path('', views.index, name='index'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('SignIn', views.SignIn, name='SignIn'),
    path('SignOut', views.SignOut, name='SignOut'),
]
