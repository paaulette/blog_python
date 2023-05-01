from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class UserExtra (models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    web = models.CharField(max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
 
    def __str__(self):
        return f"{self.user} - {self.avatar}"