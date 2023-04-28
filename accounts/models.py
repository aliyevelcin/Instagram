from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField('Image',upload_to='banners/', null=True, blank=True)
    followers = models.IntegerField(null=True, blank=True, default=0)
    following = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

# Create your models here.
