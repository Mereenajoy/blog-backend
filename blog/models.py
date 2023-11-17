from django.db import models

class PostModel(models.Model):
    userid = models.CharField(max_length=100 , default="")
    title = models.CharField(max_length=100 , default="")
    message = models.CharField(max_length=500 , default="")


class UserModel(models.Model):
    name =models.CharField(max_length=100 , default="")
    profile =models.CharField(max_length=100 , default="")
    email=models.CharField(max_length=100 , default="")
    password =models.CharField(max_length=100 , default="")