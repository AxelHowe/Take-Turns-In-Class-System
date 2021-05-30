from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    #userName = models.CharField(max_length=128)
    #classTable = models

    def __str__(self):
        return self.username
