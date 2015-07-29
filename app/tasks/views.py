from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .forms import TaskForm
from .models import Task


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


def tasks_user(request, username=''):
    return render(request, "lists/user.html", context={
        'username': username
    })


@login_required
def tasks_index(request, page_id=1):

    tasks = Task.objects.filter(user_id=request.user.id)

    return render(request, "tasks/index.html", context={
        'page_id': page_id,
        'tasks': tasks
    })


@login_required
def tasks_map(request):
    return render(request, "tasks/map.html")


@login_required
def tasks_new(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():

            # task_id omitted
            # date_created omitted
            # date_modified omitted
            data = form.cleaned_data
            data['status'] = 1
            data['user'] = request.user
            task = Task(**data)

            task.save()
            return redirect('/tasks/')
        else:
            return render(request, "tasks/new_edit.html", context={
                'form': form
            })
    else:
        form = TaskForm()

    return render(request, "tasks/new_edit.html", context={
        'form': form
    })


@login_required
def tasks_edit(request, task_id):

    if request.method == 'POST' and int(task_id) >= 1:
        task = get_object_or_404(Task, pk=task_id)
        if task.user != request.user:
            raise Http404("It's not your task mate :<")

        form = TaskForm(request.POST)
        # data = form.cleaned_data

    elif int(task_id) >= 1:
        task = get_object_or_404(Task, pk=task_id)

        form = TaskForm(initial={
            'date_from': task.date_from,
            'date_to': task.date_to,
            'description': task.description,
            'lat': task.lat,
            'lng': task.lng,
            'name': task.name,
            'place_desc': task.place_desc,
            'priority': task.priority,
            'public': task.public,
            'repeat': task.repeat,
            'repeat_days': task.repeat_days,
            'status': task.status
        })
    else:
        raise Http404("Sorry, task doesn't exist")

    return render(request, "tasks/new_edit.html", context={
        'form': form,
        'edit_task': True
    })


@login_required
def tasks_task(request, task_id):
    return render(request, "tasks/task.html", context={
        'task_id': task_id
    })

