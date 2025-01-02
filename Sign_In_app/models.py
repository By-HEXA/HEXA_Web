from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Date_of_Birth = models.DateField(null=True, blank=True)