# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Post, Comment


class PostInLine(admin.StackedInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'img']
    inlines = [PostInLine]
    list_filter = ['data']


admin.site.register(Post, PostAdmin)
