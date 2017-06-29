# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.db import models
from blog.models import Comment, Post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text', 'post_img']