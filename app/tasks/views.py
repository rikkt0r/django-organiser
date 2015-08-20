# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
# from django.views.decorators.cache import cache_page
import json
from django.views.decorators.http import require_POST

from .services import determine_file_type, require_task_ownership
from .forms import TaskForm, TaskFileForm
from .models import Task, TaskFile


# main-mega-main main site.
# @cache_page(60*10)
def index(request):
    return render(request, "index.html")


# def test_json(request):
#     from django.http import JsonResponse, HttpResponse
#     return JsonResponse({
#         'test': [],
#         'test2': {},
#         'test3': [{}, {}, {}]
#     })


def tasks_user(request, username=''):

    tasks = User.objects.get(username=username).task_set.filter(public=True).all()

    return render(request, "tasks/tasks.html", context={
        'username': username,
        'tasks': tasks
    })


@login_required
def tasks_index(request):

    tasks = Task.objects.filter(user_id=request.user.id)

    return render(request, "tasks/tasks.html", context={
        'tasks': tasks
    })


@require_task_ownership
def tasks_task(request, task_id, task=None):

    if task.user == request.user:
        context = {
            'task': task,
            'files': [1, 2, 3, 4, 5, 6, 7],
            'is_author': True
        }
    elif task.public:
        context = {
            'task': task,
            'files': [1, 2, 3, 4, 5, 6, 7],
        }
    else:
        raise Http404("It's not your task mate :<")

    return render(request, "tasks/task.html", context=context)
#
# def tasks_task(request, task_id):
#
#     task = get_object_or_404(Task, pk=task_id)
#
#     if task.user == request.user:
#         context = {
#             'task': task,
#             'files': [1, 2, 3, 4, 5, 6, 7],
#             'is_author': True
#         }
#     elif task.public:
#         context = {
#             'task': task,
#             'files': [1, 2, 3, 4, 5, 6, 7],
#         }
#     else:
#         raise Http404("It's not your task mate :<")
#
#     return render(request, "tasks/task.html", context=context)


@login_required
def tasks_map(request):

    tasks = Task.objects.exclude(lat__isnull=True, lng__isnull=True).filter(user_id=request.user.id)

    # YEAH, coz i'm tired right now..
    # ss - shit serializer
    def ss(task):
        return {
            'id': task.id,
            'name': task.name,
            'lat': str(task.lat),
            'lng': str(task.lng),
            'priority': task.priority
        }

    return render(request, "tasks/map.html", context={
        'tasks': tasks,
        'tasks_json': json.dumps([ss(i) for i in tasks])
    })


@login_required
def tasks_new(request):

    if request.method == 'POST':
        form = TaskForm(request.POST or None)

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

    if int(task_id) >= 1:

        task = get_object_or_404(Task, pk=task_id)
        if task.user != request.user:
            raise Http404("It's not your task mate :<")

        if request.method == 'POST':

            form = TaskForm(request.POST or None)
            if form.is_valid():
                for key, val in form.cleaned_data.items():
                    setattr(task, key, val)
                task.save()
                return redirect('/tasks/')
            else:
                return render(request, "tasks/new_edit.html", context={
                    'form': form,
                    'edit_task': True
                })

        else:
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

            return render(request, "tasks/new_edit.html", context={
                'form': form,
                'edit_task': True
            })
    else:
        raise Http404("Sorry, task doesn't exist")


@login_required
@require_POST
@require_task_ownership
def tasks_file_new(request, task_id, task=None):

    form = TaskFileForm(request.POST or None, request.FILES)

    if form.is_valid():

        if len(request.FILES['taskfile'].name.split('.')) == 1:
            raise ValidationError('File type is not supported')
        newfile = TaskFile(
            task=task,
            file=request.FILES['taskfile'],
            type=determine_file_type(request.FILES['taskfile'].content_type.split('/')[0]),
            size=request.FILES['taskfile']._size,
            name=form.data_cleaned['name']
        )
        newfile.save()
        return redirect()
    else:
        pass
