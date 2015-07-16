# https://docs.djangoproject.com/en/1.8/topics/http/urls/

from django.conf.urls import include, url
from django.contrib import admin

from .views import Template404View, Template500View
from tasks import views as v

handler404 = Template404View.as_view()
handler500 = Template500View.as_view()

urlpatterns = [
    url(r'^$', 'tasks.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^test/$', 'tasks.views.test_json'),

    url(r'user/(?P<username>\w+)/$', v.tasks_user, name='tasks_user'),

    url(r'tasks/$', v.tasks_index, name='tasks_index_default'),
    # url(r'tasks/(?P<task_id>[0-9]+)/$', v.tasks_index, name='tasks_index'),  NO PAGINATION.
    url(r'tasks/(?P<task_id>[0-9]+)/$', v.tasks_task, name='task'),

    url(r'tasks/map/$', v.tasks_map, name='tasks_map'),
    url(r'tasks/new/$', v.tasks_new, name='tasks_new'),
    url(r'tasks/(?P<task_id>[0-9]+)/edit/$', v.tasks_edit, name='tasks_edit')
]

