from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'HEXA_Web_Sign_up.html')