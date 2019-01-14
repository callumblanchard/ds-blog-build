from django.db import models


class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title
