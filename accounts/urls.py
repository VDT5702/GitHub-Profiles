from django.urls import path
from .views import SignUpView, UpdateProfile
from .views import ExploreView, ProfileView, MyProfileView
from django.shortcuts import render


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('explore/',ExploreView, name='explore'),
    path('profile/<int:userd_id>',ProfileView, name='profile'),
    path('profile/',MyProfileView, name='myprofile'),
    path('updatprofile/',UpdateProfile, name='update'),
]