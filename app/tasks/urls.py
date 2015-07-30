from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tasks_index, name='tasks_index'),
    url(r'^map/$', views.tasks_map, name='tasks_map'),
    url(r'^new/$', views.tasks_new, name='tasks_new'),
    url(r'^(?P<task_id>[0-9]+)/$', views.tasks_task, name='task'),
    url(r'^(?P<task_id>[0-9]+)/edit/$', views.tasks_edit, name='tasks_edit')
]
