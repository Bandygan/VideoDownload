from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    user = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    show_name = models.CharField(max_length=255, null=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=255, blank=True, default="")
    telegram_setup_code = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.user.username


class KnownEpisode(models.Model):
    is_downloaded = models.BooleanField(default=False)
    season = models.IntegerField(default=0)
    episode = models.IntegerField(default=0)
    link = models.ForeignKey(Link, related_name='episodes', on_delete=models.CASCADE)
    torrent_hash = models.CharField(max_length=255, blank=True, default="")
    last_check = models.DateTimeField(auto_now_add=True)