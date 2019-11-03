from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    text = models.CharField(max_length = 140, null = False, blank = False)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=False)