from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('notice', '공지사항'),
        ('suggestion', '건의사항'),
        ('seminar', '세미나'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 작성자
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # 카테고리 추가
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # 이미지 업로드
    file = models.FileField(upload_to='files/', blank=True, null=True)  # 파일 업로드

    def __str__(self):
        return self.title