from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=30,null=False,default="Anonymous")

class Post(models.Model):
    title = models.CharField(max_length=100,null=False)
    discription = models.CharField(max_length=250,null=False)
    # created_on = models.DateTimeField(auto_now_add=True)

