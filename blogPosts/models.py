from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400, default="Subtitle")
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default="Body")

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('blogPosts:post-detail', kwargs={'post_id': self.pk})
