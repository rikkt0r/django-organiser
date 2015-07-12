# https://docs.djangoproject.com/en/1.8/topics/http/urls/

from django.conf.urls import include, url
from django.contrib import admin

from .views import Template404View, Template500View
from organiser import views as v

handler404 = Template404View.as_view()
handler500 = Template500View.as_view()

urlpatterns = [
    url(r'^$', 'organiser.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^test/$', 'organiser.views.test_json'),

    url(r'lists/$', v.lists_index, name='lists_index_default'),
    url(r'lists/(?P<page_id>[0-9]+)/$', v.lists_index, name='lists_index'),
    url(r'lists/(?P<username>\w+)/$', v.lists_user, name='lists_user'),
    url(r'lists/search/(?P<username>\w+)/$', v.lists_search, name='lists_search'),

    url(r'tasks/$', v.tasks_index, name='tasks_index_default'),
    url(r'tasks/(?P<task_id>[0-9]+)/$', v.tasks_index, name='tasks_index'),
    url(r'tasks/map/$', v.tasks_map, name='tasks_map'),
    url(r'tasks/task/new/$', v.tasks_task_new, name='tasks_task_new'),
    url(r'tasks/task/edit/(?P<task_id>[0-9]+)/$', v.tasks_task_edit, name='tasks_task_edit'),
    url(r'tasks/task/task/(?P<task_id>[0-9]+)/$', v.tasks_task, name='tasks_task')
]

