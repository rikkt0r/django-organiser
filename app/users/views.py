from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm


@login_required
def users_index(request):

    return render(request, "users/panel.html")


def users_login(request):

    if request.method == 'GET':
        return render(request, "users/login.html", context={
            'login_form': LoginForm
        })

    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/tasks/')
                else:
                    return render(request, "users/login.html", context={
                        'error': 'disabled account, you idjit',
                        'login_form': LoginForm,
                        'invalid_login': 'error'
                    })
            else:
                return render(request, "users/login.html", context={
                    'error': 'Incorrect password',
                    'login_form': LoginForm,
                    'invalid_password': 'error'
                })
        else:
            return render(request, "users/login.html", context={
                'error': 'type CORRECT login...',
                'login_form': LoginForm,
                'invalid_login': 'error'
            })


def users_logout(request):
    logout(request)
    return redirect('/')


def users_passwd(request):
    return render(request, "users/passwd.html")


def users_settings(request):
    return render(request, "users/settings.html")

