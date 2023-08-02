from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=225)
    number=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    emailid=models.EmailField()
   
class source(models.Model):
    name=models.CharField(max_length=225)
    img=models.ImageField(upload_to='pics')
    discription=models.CharField(max_length=500)

class animemovie(models.Model):
    name=models.CharField(max_length=225)
    img=models.ImageField(upload_to='pics')
    discription=models.CharField(max_length=500)
    