# models.py

from django.contrib.auth.models import User
from django.db import models

class Link(models.Model):
    user = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
