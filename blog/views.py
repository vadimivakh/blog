# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Post, Comment


def index(request):
    return render_to_response('main.html')


def all_posts(request):
    return render_to_response('all_posts.html', {'posts': Post.objects.all()})


def post_by_id(request, post_id=1):
    return render_to_response('post_by_id.html', {'post': Post.objects.get(id=post_id), 'comments': Comment.objects.filter(comment_post_id=post_id)})
    # return render_to_response('post_by_id.html', {'post': Post.objects.get(id=post_id)})