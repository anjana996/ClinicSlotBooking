from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PatientProfile(models.Model):
    user=models.CharField(max_length=120)
    age=models.IntegerField()
    bloodgroup=models.CharField(max_length=5)
    address=models.CharField(max_length=150)
    phonenumber=models.IntegerField(max_length=12,unique=True)






    def __str__(self):
        return self.user

