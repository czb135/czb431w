
from django.db import models
from django.contrib.auth.models import AbstractUser
class Users(AbstractUser):
    email = models.TextField('email')
    password = models.TextField('password')

