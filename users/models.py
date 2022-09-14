from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    username = models.EmailField("Email", unique=True)
    REQUIRED_FIELDS = []
