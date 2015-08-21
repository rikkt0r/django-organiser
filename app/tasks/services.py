# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import available_attrs
from django.http import HttpResponseNotAllowed
from django.conf import settings
from functools import wraps

from .models import Task


def ssl_required(fn):
    @wraps(fn)
    def decorated_view(request, *args, **kwargs):
        if settings.SSL_REQUIRED:
            if request.is_secure:
                return fn(*args, **kwargs)
            else:
                return redirect(request.url.replace("http://", "https://"))
        return fn(*args, **kwargs)
    return decorated_view


def require_task_ownership(func):

    @wraps(func, assigned=available_attrs(func))
    def decorator(request, *args, **kwargs):
        task_id = int(kwargs.get('task_id'))
        if int(task_id) >= 1:
            task = get_object_or_404(Task, pk=task_id)
            if task.user != request.user:
                return HttpResponseNotAllowed("Task doesn't exist or you are not an owner")
            else:
                kwargs['task'] = task
        else:
            return HttpResponseNotAllowed("Task doesn't exist or you are not an owner")

        return func(request, *args, **kwargs)
    return decorator


def determine_file_type(filename):
    # TYPES = (
    #     (0, 'Unknown'),
    #     (1, 'Image'),
    #     (2, 'Audio'),
    #     (3, 'Video')
    #     (4, 'Document')
    # )

    if any('.'+s in filename for s in settings.TASK_UPLOAD_FILE_IMAGE):
        return 1
    if any('.'+s in filename for s in settings.TASK_UPLOAD_FILE_AUDIO):
        return 2
    if any('.'+s in filename for s in settings.TASK_UPLOAD_FILE_VIDEO):
        return 3
    if any('.'+s in filename for s in settings.TASK_UPLOAD_FILE_DOCUMENT):
        return 4
    else:
        return 0
