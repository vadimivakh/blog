from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


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
    post_data = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, default="")
    post_likes = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    post_img = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Image')

    def __unicode__ (self):
        return self.post_title


class Comment(models.Model):
    class Meta:
        db_table = "comments"

    comment_date = models.DateField(u'date', auto_now=True)
    comment_text = models.TextField(verbose_name=None)
    comment_post = models.ForeignKey(Post)
    comment_author = models.ForeignKey(User, default="")

