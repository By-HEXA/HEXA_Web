from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('board/', include('board.urls')),  # /board/ URL 연결
    path('admin/', admin.site.urls),
]
