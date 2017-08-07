# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Post, Comment, Tag


class PostInLine(admin.StackedInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fields = ['post_title', 'post_text', 'post_img']
    inlines = [PostInLine]
    list_filter = ['post_data']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)