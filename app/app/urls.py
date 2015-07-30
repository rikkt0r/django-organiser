# https://docs.djangoproject.com/en/1.8/topics/http/urls/

from django.conf.urls import include, url
from django.contrib import admin

from .views import Template404View, Template500View

handler404 = Template404View.as_view()
handler500 = Template500View.as_view()

urlpatterns = [
    url(r'^$', 'tasks.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^tasks/', include('tasks.urls', namespace='tasks')),
    url(r'^user/(?P<username>\w+)/$', 'tasks.views.tasks_user', name='tasks_user')
]

