from django.shortcuts import render
from django.contrib.auth.models import User
from loginsys.models import UserProfile
from blog.models import Post, Comment
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from loginsys.models import UserProfile
from django.contrib import auth
from django.template.context_processors import csrf
from loginsys.forms import UserProfileForm


def user_profile(request, user_id):
    context = {}
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user_id=user_id)
    context['user'] = user
    context['profile'] = profile
    context['username'] = auth.get_user(request).username
    context['user_id'] = request.user.id
    context['user_posts'] = Post.objects.filter(post_author = request.user.id).order_by('-post_data')
    context['user_post_counter'] = Post.objects.filter(post_author = request.user.id).count()
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