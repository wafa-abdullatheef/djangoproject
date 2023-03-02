from django.db import models

class Signup(models.Model):
    Name=models.CharField(max_length=16)
    Age=models.IntegerField()
    Place=models.CharField(max_length=16)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
class Gallery(models.Model):
    Name=models.CharField(max_length=16)
    Age=models.IntegerField()
    Place=models.CharField(max_length=16)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
