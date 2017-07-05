from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib import auth
# from loginsys.forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm

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
            args['login_error'] = 'User not found'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def register(request):
    print('start')
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()


    if request.POST:
        print('post')
        new_user_form = UserCreationForm(request.POST or None)
        print (new_user_form.is_valid(), new_user_form.errors, type(new_user_form.errors))
        if new_user_form.is_valid():
            print('valid')
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password1'])
            auth.login(request, new_user)
            print('here')
            return redirect('/')
    return render_to_response('register.html', args)