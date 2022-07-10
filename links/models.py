from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    origin_link = models.URLField(unique=True)
    shortened_link = models.URLField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')
