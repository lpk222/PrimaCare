from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    disease = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username + " - patient"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username + " - doctor"