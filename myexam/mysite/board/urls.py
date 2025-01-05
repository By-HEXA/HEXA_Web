from django.urls import path
from . import views

app_name = 'board'  # 앱 네임스페이스 설정
urlpatterns = [
    path('', views.index, name='index'),  # 빈 경로를 index 뷰에 매핑
]
