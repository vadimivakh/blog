from django.shortcuts import render
from django.contrib.auth.models import User
from loginsys.models import UserProfile
from django.shortcuts import get_object_or_404
from blog.models import Post, Comment
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from loginsys.models import UserProfile
from django.contrib import auth
from django.template.context_processors import csrf
from loginsys.forms import UserProfileForm
from django.http import Http404


def user_profile(request, user_id):
    context = {}

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("User with \'id={}\' does not exists".format(user_id))

    try:
        profile = UserProfile.objects.get(user_id=user_id)
    except UserProfile.DoesNotExist:
        raise Http404("User's Profile with \'id={}\' does not exists".format(user_id))

    profile = get_object_or_404(UserProfile, user_id=user_id)
    context['user'] = user
    context['profile'] = profile
    context['username'] = auth.get_user(request).username
    context['user_id'] = request.user.id
    context['user_posts'] = Post.objects.filter(author = request.user.id).order_by('-data')
    context['user_post_counter'] = Post.objects.filter(author = request.user.id).count()
    context['user_comments'] = Comment.objects.filter(comment_author_id=user_id)
    return render_to_response('profile.html', context)


def edit_user_profile(request, user_id):
    context = {}
    context.update(csrf(request))
    context['user'] = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user_id=user_id)
    context['profile'] = profile
    context['form'] = UserProfileForm(instance=profile)
    context['user_id'] = request.user.id

    if request.POST:
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/members/{}'.format(request.user.id))

    return render_to_response('edit_profile.html', context)


def user_posts(request, user_id):
    context = {}
    context.update(csrf(request))
    context['user_id'] = request.user.id
    context['user_posts'] = Post.objects.filter(author=request.user.id).order_by('-data')
    context['username'] = auth.get_user(request).username
    return render_to_response('posts_by_user.html', context)


def user_comments(request, user_id):
    context = {}
    context.update(csrf(request))
    context['user_id'] = request.user.id
    context['user_comments'] = Comment.objects.filter(comment_author_id=user_id)
    context['username'] = auth.get_user(request).username
    return render_to_response('comments_by_user.html', context)


def delete_profile(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')
