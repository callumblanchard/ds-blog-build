from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import requests


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save(**kwargs)
'''
        img = Image.open(requests.get(self.profile_image.url, stream=True).raw)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.url)
'''
