from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import UserProfile,Repository

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Repository)