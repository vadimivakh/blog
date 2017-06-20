# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    class Meta:
        db_table = "post"

    post_title = models.CharField(max_length = 100)
    post_text = models.TextField()
    post_data = models.DateTimeField()
    post_likes = models.IntegerField()

