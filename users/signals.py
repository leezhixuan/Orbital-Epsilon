from django.db.models.signals import post_save
from django.contrib.auth.models import User
from models import Profile
from django.db import models

def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = Profile(user=user)
        profile.save()

post_save.connect(create_profile, sender=User, dispatch_uid="users-profilecreation-signal")
