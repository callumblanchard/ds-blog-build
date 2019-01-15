from django.db import models


class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400, default="Subtitle")
    pub_date = models.DateTimeField('Published ')
    author = models.CharField(max_length=25, default="Author")
    body = models.TextField(default="Body")

    def __str__(self):
        return self.post_title
