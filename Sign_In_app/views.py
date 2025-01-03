from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from datetime import datetime

def SignIn(request):
    if request.method == 'POST':
        username = request.POST['ID']
        password = request.POST['PassWord']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'HEXA_Web_Sign_In.html')
        else:
            return render(request, 'HEXA_Web_Sign_In.html')
    return render(request, 'HEXA_Web_Sign_In.html')

def SignOut(request):
    logout(request)
    return redirect('Sign_app:SignIn')

def SignUp(request):
    if request.method == 'POST':
        username = request.POST['ID']
        password = request.POST['PW']
        lastname = request.POST['Lastname']
        firstname = request.POST['Firstname']
        BR = request.POST['BR']
        date = datetime.strptime(BR, "%Y.%m.%d").date()
        si = request.POST['SI']
        school = request.POST['School']
        major = request.POST['Major']
        mail = request.POST['Mail']
        user = User.objects.create_user(username=username, password=password, 
            last_name=lastname, first_name=firstname, Date_of_Birth=date, 
            School=school, Major=major, Student_ID=si, email=mail)
        user.save()
        return redirect('Sign_app:SignIn')
    
    return render(request, 'HEXA_Web_Sign_up.html')