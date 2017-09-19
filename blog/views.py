# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from blog.models import Post, Comment
from blog.forms import CommentForm, PostForm, EditPostForm
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User


def all_posts(request):
    post_list = Post.objects.all().order_by('-data')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    form = PostForm(request.POST)
    context = {}
    context.update(csrf(request))
    context['username'] = auth.get_user(request).username
    context['posts'] = posts
    context['form'] = form
    context['post_counter'] = Post.objects.count()
    context['user_counter'] = User.objects.count()
    context['user_id'] = request.user.id
    return render_to_response('all_posts.html', context)


def post_by_id(request, post_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    item = get_object_or_404(Post, id=post_id)
    item.views += 1
    item.save()
    args['post'] = Post.objects.get(id=post_id)
    args['comments'] = Comment.objects.filter(comment_post_id=post_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    args['post_creator'] = False
    args['user_id'] = request.user.id
    if str(auth.get_user(request).username) == str(
            Post.objects.get(id=post_id).author) and request.user.is_authenticated():
        args['post_creator'] = True
    return render_to_response('post_by_id.html', args)


def add_comment(request, post_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_author = request.user
            comment.comment_post = Post.objects.get(id=post_id)
            form.save()
    return redirect('/posts/{}/'.format(post_id))


def add_post(request):
    if request.POST:
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
    return redirect('/', RequestContext(request))


def login(request):
    return render_to_response('login.html')


def edit_post(request, post_id):
    args = {}
    args.update(csrf(request))
    post = Post.objects.get(id=post_id)
    args['post'] = get_object_or_404(Post, id=post_id)
    args['form'] = EditPostForm(instance=post)
    args['username'] = auth.get_user(request).username
    args['user_id'] = request.user.id

    if request.POST:
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/posts/{}/'.format(post_id))
    return render_to_response('edit_post.html', args)


def delete_post(request, post_id):
    Post.objects.get(id=post_id).delete()
    Comment.objects.filter(comment_post_id=post_id).delete()
    return redirect('/')


def post_by_tag(request, tag_name):
    context = {}
    context = {'post_by_tag_list': Post.objects.filter(tags__name=tag_name)}
    context['tag_name'] = tag_name
    context['username'] = auth.get_user(request).username
    context['user_id'] = request.user.id

    return render_to_response('posts_by_tag.html', context)
