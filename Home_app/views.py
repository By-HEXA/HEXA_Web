from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render(request, 'HEXA_Web_Door.html')

def Home(request):
    return render(request, 'HEXA_Web_Home.html')