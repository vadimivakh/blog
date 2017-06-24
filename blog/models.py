# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# class Tag(models.Model):
# 	name = models.CharField(max_length=50)
#
# 	def __unicode__(self):
# 		return self.name


class Post(models.Model):
    class Meta:
        db_table = "post"

    post_title = models.CharField(max_length = 100)
    post_text = models.TextField()
    post_data = models.DateTimeField()
    # post_author = models.ForeighKey(User)
    post_likes = models.IntegerField(default=0)


class Comment(models.Model):
    class Meta:
        db_table = "comments"

    comment_text = models.TextField(verbose_name=None)
    comment_post = models.ForeignKey(Post)

