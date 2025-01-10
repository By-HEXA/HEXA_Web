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
from Home_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Home_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('Home', views.Home, name='Home'),
    path('Found', views.Found, name='Found'),
    path('Member', views.Member, name='Member'),
    path('Suggest', views.Suggest, name='Suggest'),
    path('Notice', views.Notice, name='Notice'),
    path('Seminar', views.Seminar, name='Seminar'),
    path('Notice_write', views.Notice_write, name='Notice_write'),
    path('Notice_detail', views.Notice_detail, name='Notice_detail'),
    path('Notice_edit', views.Notice_edit, name='Notice_edit'),
    path('Notice_write', views.Notice_write, name='Notice_write'),
    path('Notice/<int:post_id>', views.Notice_detail, name='Notice_detail'),
    path('Notice/<int:post_id>/edit/', views.Notice_edit, name='Notice_edit'),  # 수정 페이지
    path('Notice/<int:post_id>/delete/', views.Notice_delete, name='Notice_delete'),  # 삭제 페이지
    path('Idea', views.Idea, name='Idea'),
    path('Team', views.Team, name='Team'),
    path('Suggest_write', views.Suggest_write, name='Suggest_write'),
    path('Suggest_detail', views.Suggest_detail, name='Suggest_detail'),
    path('Suggest_edit', views.Suggest_edit, name='Suggest_edit'),
    path('Suggest_write', views.Suggest_write, name='Suggest_write'),
    path('Suggest/<int:post_id>', views.Suggest_detail, name='Suggest_detail'),
    path('Suggest/<int:post_id>/edit/', views.Suggest_edit, name='Suggest_edit'),  # 수정 페이지
    path('Suggest/<int:post_id>/delete/', views.Suggest_delete, name='Suggest_delete'),  # 삭제 페이지
    path('Seminar_write', views.Seminar_write, name='Seminar_write'),
    path('Seminar_detail', views.Seminar_detail, name='Seminar_detail'),
    path('Seminar_edit', views.Seminar_edit, name='Seminar_edit'),
    path('Seminar_write', views.Seminar_write, name='Seminar_write'),
    path('Seminar/<int:post_id>', views.Seminar_detail, name='Seminar_detail'),
    path('Seminar/<int:post_id>/edit/', views.Seminar_edit, name='Seminar_edit'),  # 수정 페이지
    path('Seminar/<int:post_id>/delete/', views.Seminar_delete, name='Seminar_delete'),  # 삭제 페이지
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)