from django.db import models

# Create your models here.

class SignUpModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

class LoginModel(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

class BuyInfoModel(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.TextField()
    description = models.TextField(null=True)

class ContacUstModel(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
