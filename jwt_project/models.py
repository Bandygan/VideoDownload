from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    user = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=255, blank=True, default="")
    telegram_setup_code = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.user.username
