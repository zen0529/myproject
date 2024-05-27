from django.contrib.auth.models import AbstractUser
from django.db import models

from myproject import settings

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)

class SentimentAnalysis(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    sentiment = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.user.username} - {self.sentiment}"