# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from blog.models import Comment, Post
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model = Comment

        fields = ['comment_text']
        widgets = {
            'comment_text': Textarea(attrs={'cols': 40, 'rows': 3}),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ['post_title',
                  'post_text',
                  'post_img',
                  'tags']
        labels = {"post_title": "Title:",
                    "post_text": "Text:",
                    "post_img": "Add image:",
                    "tags": "Tags"}
        widgets = {
            'post_title': Textarea(attrs={'cols': 70, 'rows': 1}),
            'post_text': Textarea(attrs={'cols': 70, 'rows': 5}),
            'tags': Textarea(attrs={'cols': 40, 'rows': 1}),
        }

