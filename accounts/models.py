from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from datetime import datetime
import requests

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    fullname = models.CharField(max_length=50,default='')
    no_followers = models.IntegerField(default=0)
    lastupdated = models.DateTimeField(default=datetime.now, blank = True)

    def __str__(self):
        return f'{self.user.username}'



class Repository(models.Model):
    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    repo_name = models.CharField(max_length = 50,default='')
    no_stars = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.repo_name}'
