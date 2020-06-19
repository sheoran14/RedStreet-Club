from django.db import models
from django .forms import forms
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='default')
    venue = models.CharField(max_length=100)
    message = models.TextField()
    cash = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)

class Power(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    message = models.TextField()
    cash = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
class Body(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    message = models.TextField()
    cash = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
class Badminton(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    message = models.TextField()
    cash = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
class Ttennis(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    message = models.TextField()
    cash = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
class Chess(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    message = models.TextField()
    cash = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)



class Makep(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    city = models.CharField(max_length=100)
    zip = models.IntegerField()
    amount = models.IntegerField()
    card = models.IntegerField()

