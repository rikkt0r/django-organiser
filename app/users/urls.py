from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.users_index, name='index'),
    # url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    url(r'^login/$', views.users_login, name='login'),
    url(r'^logout/$', views.users_logout, name='logout'),
    url(r'^passwd/$', views.users_passwd, name='passwd')
]
