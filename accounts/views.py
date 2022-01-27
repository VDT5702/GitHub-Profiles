from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse
from accounts.models import UserProfile, Repository
import requests


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def ExploreView(request):
    context = {'Users':UserProfile.objects.all(), 'Repos': Repository.objects.all()  }
    return render(request, 'explore.html',context) 


def ProfileView(request, userd_id):
    userd_id +=1
    user1 = UserProfile.objects.get(id=userd_id)
    context = {'User':user1, 'Repos': Repository.objects.filter(userprofile=user1) , 'uid': userd_id-1 }
    return render(request, 'profile.html', context)

def MyProfileView(request):
    curr_user = request.user
    uid = curr_user.id
    uid-=1
    # profile = UserProfile.objects.filter(id = uid)
    # context = {'profile': profile}
    # return render(request,'myprofile.html', context)
    return ProfileView(request, uid)

def UpdateProfile(request):
    user = request.user

    profile = UserProfile.objects.filter(user = user)

    profile.delete()

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

    return 
         