# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    class Meta:
        db_table = "post"

    post_title = models.CharField(max_length = 100)
    post_text = models.TextField()
    post_data = models.DateTimeField()
    post_likes = models.IntegerField(default=0)

class Comment(models.Model):
    class Meta:
        db_table = "comments"

    comment_text = models.TextField()
    comment_post = models.ForeignKey(Post)

