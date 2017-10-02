# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from blog.models import Post, Comment
from blog.forms import CommentForm, PostForm, EditPostForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView


class PostListView(ListView):
    template_name = 'post_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update(csrf(self.request))
        context['username'] = auth.get_user(self.request).username
        context['form'] = PostForm(self.request.POST)
        context['post_counter'] = Post.objects.count()
        context['user_counter'] = User.objects.count()
        context['user_id'] = self.request.user.id
        return context

    def get_queryset(self):
        return Post.objects.all().order_by('-data')


class PostDetailView(DetailView):
    template_name = 'post_by_id.html'
    model = Post
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        item = get_object_or_404(Post, id=self.kwargs['post_id'])
        item.views += 1
        item.save()
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update(csrf(self.request))
        context['comments'] = Comment.objects.filter(comment_post_id=self.kwargs['post_id'])
        context['form'] = CommentForm
        context['username'] = auth.get_user(self.request).username
        context['post_creator'] = False
        context['user_id'] = self.request.user.id
        if str(auth.get_user(self.request).username) == str(
                Post.objects.get(id=self.kwargs['post_id']).author) and self.request.user.is_authenticated():
            context['post_creator'] = True
        return context


class CreateCommentView(CreateView):
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        form.instance.comment_post = Post.objects.get(id=self.kwargs['post_id'])
        return super(CreateCommentView, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class CreatePostView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePostView, self).form_valid(form)


def login(request):
    return render_to_response('login.html')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'
    success_url = '/'
    pk_url_kwarg = 'post_id'


def delete_post(request, post_id):
    Post.objects.get(id=post_id).delete()
    Comment.objects.filter(comment_post_id=post_id).delete()
    return redirect('/')


class TagPostList(ListView):
    template_name = 'tag_posts_list.html'
    context_object_name = 'tag_list'

    def get_context_data(self, **kwargs):
        context = super(TagPostList, self).get_context_data(**kwargs)
        context['username'] = auth.get_user(self.request).username
        context['user_id'] = self.request.user.id
        context['tag_name'] = self.kwargs['tag_name']
        return context

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs['tag_name'])
