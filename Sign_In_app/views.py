from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from datetime import datetime
from django.contrib import messages
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def SignIn(request):
    if request.method == 'POST':
        username = request.POST['ID']
        password = request.POST['PassWord']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'HEXA_Web_Home.html')
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
        if User.objects.filter(username = username).exists():
            messages.error(request, '이미 존재하는 ID입니다. 다른 ID를 입력하세요.')
            return render(request, 'HEXA_Web_Sign_up.html')
        # if User.objects.filter(username=username).exists():
        #     return JsonResponse({'exists': True})
        user = User.objects.create_user(username = username, password = password, 
            last_name = lastname, first_name = firstname, Date_of_Birth = date, 
            School =school, Major = major, Student_ID = si, email = mail)
        user.save()
        return redirect('Sign_app:SignIn')    
    return render(request, 'HEXA_Web_Sign_up.html')

# @login_required
def DeleteAccount(request):
    if request.method == 'POST':
        username = request.POST['ID']
        password = request.POST['PW']
        si = request.POST['SI']
        user = request.user
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is None:
            messages.error(request, "정보와 일치하는 사용자를 찾을 수 없습니다.")
            return redirect('Sign_app:DeleteAccount')
        if authenticated_user != request.user:
            messages.error(request, "현재 로그인된 계정만 탈퇴할 수 있습니다.")
            return redirect('Sign_app:DeleteAccount')
        try:
            user_with_si = User.objects.get(username=username, Student_ID=si)
            if user_with_si == request.user:
                user.delete()
                return render(request, 'HEXA_Web_Alert_Delete.html')
            else:
                messages.error(request, "정보와 일치하는 사용자를 찾을 수 없습니다.")
                return redirect('Sign_app:DeleteAccount')
        except User.DoesNotExist:
            messages.error(request, "정보와 일치하는 사용자를 찾을 수 없습니다.")
            return redirect('Sign_app:DeleteAccount')
    return render(request, 'HEXA_Web_Delete.html')

def Find_ID(request):
    if request.method == 'POST':
        user_si = request.POST['SI']
        Lastname = request.POST['Lastname']
        Firstname = request.POST['Firstname']
        try:
            user = User.objects.get(Student_ID = user_si, last_name = Lastname, first_name = Firstname)
            find_username = user.username
            return render(request, 'HEXA_Web_Alert_ID.html', {
                'find_id': find_username,
                'find_name': Lastname + Firstname
            })
        except User.DoesNotExist:
            messages.error(request, "정보와 일치하는 사용자를 찾을 수 없습니다.")
            return render(request, 'HEXA_Web_Find.html')
    return render(request, 'HEXA_Web_Find.html')

def Check_ID(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data.get('ID')
        exists = User.objects.filter(username=user_id).exists()
        return JsonResponse({'exists': exists})