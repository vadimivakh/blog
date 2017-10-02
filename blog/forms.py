# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from blog.models import Comment, Post
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model = Comment

        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'cols': 40, 'rows': 3}),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ['title',
                  'text',
                  'img',
                  'tags']
        labels = {"title": "Title:",
                  "text": "Text:",
                  "img": "Add image:",
                  "tags": "Tags"}
        widgets = {
            'title': Textarea(attrs={'cols': 55, 'rows': 1}),
            'text': Textarea(attrs={'cols': 55, 'rows': 5}),
            'tags': Textarea(attrs={'cols': 55, 'rows': 1}),
        }


class EditPostForm(ModelForm):
    class Meta:
        model = Post

        fields = ['title',
                  'text',
                  'img']
        labels = {"title": "Title:",
                  "text": "Text:",
                  "img": "Add image:"}
        widgets = {
            'title': Textarea(attrs={'cols': 100, 'rows': 1}),
            'text': Textarea(attrs={'cols': 100, 'rows': 20})}
