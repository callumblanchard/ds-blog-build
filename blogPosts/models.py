from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400, default="Subtitle")
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default="Body")
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, default='', unique=True)

    def __str__(self):
        return self.post_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title)
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogPosts:post-detail', kwargs={
            'slug': self.slug,
        })

    def get_publish_url(self):
        return reverse('blogPosts:publish', kwargs={
            'slug': self.slug,
        })


class Comment(models.Model):
    post = models.ForeignKey('blogPosts.BlogPost', on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
