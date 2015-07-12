from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
# from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy

# main-mega-main main site.
# @cache_page(60*10)
def index(request):
    return render(request, "index.html")

def test_json(request):
    return JsonResponse({
        'test': [],
        'test2': {},
        'test3': [{}, {}, {}]
    })

def tasks(request):
    
    ctx = dict()
    ctx['csrf_input'] = csrf_input_lazy(request)
    ctx['csrf_token'] = csrf_token_lazy(request)
    ctx['task_list'] = [{'id': i, 'name': 'task '+str(i)} for i in range(15)]

    return render(request, "organiser/tasks.html", ctx)


def lists_index(request, page_id=1):
    return render(request, "lists/index.html")

def lists_search(request, username=''):
    return render(request, "lists/index.html", context={
        'username': username
    })

def lists_user(request, username=''):
    return render(request, "lists/user.html", context={
        'username': username
    })

@login_required
def tasks_index(request, page_id=1):
    return render(request, "tasks/index.html", context={
        'page_id': page_id
    })

@login_required
def tasks_map(request):
    return render(request, "tasks/map.html")

@login_required
def tasks_task_new(request):
    return render(request, "tasks/task_new.html")

@login_required
def tasks_task_edit(request, task_id):
    return render(request, "tasks/task_edit.html", context={
        'task_id': task_id
    })

@login_required
def tasks_task(request, task_id):
    return render(request, "tasks/task.html", context={
        'task_id': task_id
    })

