
from django.db import models
from django.contrib.auth.models import AbstractUser
class Users(AbstractUser):
    email = models.TextField('email', max_length=100)
    password = models.TextField('password', max_length=100)

