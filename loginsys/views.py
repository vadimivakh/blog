from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Incorrect username or password'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    # return_path = request.META.get('HTTP_REFERER', '/')
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form_user'] = UserCreationForm()
    args['form_profile'] = UserProfileForm()

    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        new_user_profile = UserProfileForm(request.POST, request.FILES)

        if new_user_form.is_valid():
            new_user = new_user_form.save()
            print(new_user)

        if new_user_profile.is_valid():
            profile = new_user_profile.save(commit=False)
            profile.user = new_user
            profile.save()

            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password1'])
            auth.login(request, new_user)
            return redirect('/')
    return render_to_response('register.html', args)