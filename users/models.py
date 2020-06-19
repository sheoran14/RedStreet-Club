from django.db import models

# Create your models here.


class Post(models.Model):
    user_name = models.CharField(max_length=200, null=False)
    sport_name = models.CharField(max_length=200, null=False)
    post_message = models.TextField(default='tutorial content')

    registration_date = models.DateField(blank=True, null=True)
    user_profile_link = models.URLField(blank=True, null=True)

class Coach(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    sport_name = models.CharField(max_length=200, null=True)
    contact = models.IntegerField()
    city = models.CharField(max_length=100)