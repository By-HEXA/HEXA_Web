from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Date_of_Birth = models.DateField(null=True, blank=True)
    School = models.CharField(max_length=50, null=True, blank=True)
    Major = models.CharField(max_length=50, null=True, blank=True)
    Student_ID = models.CharField(max_length=50, null=True, blank=True)