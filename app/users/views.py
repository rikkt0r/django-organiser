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
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if form.is_valid():
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, "users/login.html", context={
                    'error': 'disabled account, you idjit'
                })
        else:
            return render(request, "users/login.html", context={
                'error': 'type CORRECT login....'
            })


def users_logout(request):
    logout(request)
    return redirect('/')

def users_passwd(request):
    return render(request, "users/passwd.html")

