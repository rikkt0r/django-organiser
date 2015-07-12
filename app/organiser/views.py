from django.shortcuts import render
from django.http import JsonResponse
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy


def index(request):
    return render(request, "index.html")


def tasks(request):

    ctx = dict()
    ctx['csrf_input'] = csrf_input_lazy(request)
    ctx['csrf_token'] = csrf_token_lazy(request)
    ctx['task_list'] = [{'id': i, 'name': 'task '+str(i)} for i in range(15)]

    return render(request, "organiser/tasks.html", ctx)


def tasks_overview(request):
    return render(request, "organiser/tasks_overview.html")


def tasks_map(request):
    return render(request, "organiser/tasks_map.html")


def task_view(request):
    return render(request, "organiser/task.html")


# add / edit
def task_add(request):
    return render(request, "organiser/task_add.html")


def panel(request):
    return render(request, "organiser/panel.html")

# login, logout ==> contrib.auth


def test_json(request):
    return JsonResponse({
        'test': [],
        'test2': {},
        'test3': [{}, {}, {}]
    })
