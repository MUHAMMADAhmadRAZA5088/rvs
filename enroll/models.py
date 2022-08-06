import email
from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)