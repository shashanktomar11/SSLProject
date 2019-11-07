from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    first_name = models.TextField()

    last_name = models.TextField()

    email = models.EmailField()

    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
