# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from blog.models import Post, Comment
from django.core.exceptions import ObjectDoesNotExist
from blog.forms import CommentForm
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.views.generic import ListView
from django.contrib import auth

def all_posts(request):
    return render_to_response('all_posts.html', {'posts': Post.objects.all().order_by('-post_data'), 'username': auth.get_user(request).username})


def post_by_id(request, post_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['post'] = Post.objects.get(id=post_id)
    args['comments'] = Comment.objects.filter(comment_post_id=post_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('post_by_id.html', args)

def add_like(request, post_id):
    try:
        post = Post.objects.get(id = post_id)
        post.post_likes += 1
        post.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def add_comment(request, post_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post=Post.objects.get(id=post_id)
            form.save()
    return redirect('/posts/{}/'.format(post_id))

def login(request):
    return render_to_response('login.html')