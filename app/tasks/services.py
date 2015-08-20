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

    task = None

    @wraps(func, assigned=available_attrs(func))
    def decorator(request, *args, **kwargs):
        task_id = int(kwargs.get('task_id'))
        if int(task_id) >= 1:
            t = get_object_or_404(Task, pk=task_id)
            if t.user != request.user:
                return HttpResponseNotAllowed("Task doesn't exist or you are not an owner")
            else:
                global task
                task = t
        else:
            return HttpResponseNotAllowed("Task doesn't exist or you are not an owner")

        return func(request, *args, **kwargs)
    decorator.task = task
    return decorator


def owner_required(Model=None):
    """
    Usage:

    @permission_required('blogs.change_entry')
    @owner_required(Entry)
    def manage_entry(request, object_id=None, object=None):

    @permission_required('blogs.delete_entry')
    @owner_required()
    def entry_delete(*args, **kwargs):
        kwargs["post_delete_redirect"] = reverse('manage_blogs')
        return delete_object(*args, **kwargs)
    """
    def _decorator(viewfunc):
        def _closure(request, *args, **kwargs):
            user = request.user
            grant = False
            model = Model
            mod_edit = False
            if 'object_id' in kwargs:
                object_id = int(kwargs['object_id'])
                if model:
                    mod_edit = True
                elif 'model' in kwargs:
                    model = kwargs['model']
                object = get_object_or_404(model, pk=object_id)

                if user.is_superuser:
                    grant = True
                else:
                    if user.__class__ == model:
                        grant = object_id == user.id
                    else:
                        names = [rel.get_accessor_name() for rel in user._meta.get_all_related_objects() if rel.model == model]
                        if names:
                            grant = object_id in [o.id for o in eval('user.%s.all()' % names[0])]
                if not grant:
                    response = render_to_response("403.html", {'object': object}, context_instance=RequestContext(request))
                    response.status_code = 403
                    return response
                if mod_edit:
                    kwargs['object'] = object

            response = viewfunc(request, *args, **kwargs)
            return response

        return wraps(viewfunc)(_closure)
    return _decorator


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
