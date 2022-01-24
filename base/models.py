from statistics import mode
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline