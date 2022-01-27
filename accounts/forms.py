from datetime import datetime
from .models import Repository, UserProfile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import requests

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
    
    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit=False)

        if commit:
            user.save()
        
        username = user.get_username()
        fullname = user.get_full_name()
        response = requests.get(f"https://api.github.com/users/{username}")
        respdict = response.json()
        no_followers=respdict['followers']
        
        newprofile = UserProfile(user = user, fullname = fullname, no_followers = no_followers, lastupdated = respdict['updated_at'])
        newprofile.save()

        resp2 = requests.get(f"https://api.github.com/users/{username}/repos").json()
    
        for i in resp2:
            newrepo = Repository(userprofile = newprofile, repo_name = i['name'], no_stars = i['stargazers_count'])
            newrepo.save()

        
        return user


