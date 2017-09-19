from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
    # class Meta:
    #     db_table = "post"

    title = models.CharField(max_length=100)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default="")
    views = models.IntegerField(default=0)
    img = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Image')
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    # class Meta:
    #     db_table = "comments"

    date = models.DateTimeField(u'date', auto_now=True)
    text = models.TextField()
    comment_post = models.ForeignKey(Post)
    comment_author = models.ForeignKey(User, null=True)