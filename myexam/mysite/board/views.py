from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    print("Index view is called!")
    return HttpResponse("Index view is working!")  # 간단한 응답 반환