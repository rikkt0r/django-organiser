"""

https://docs.djangoproject.com/en/1.8/topics/http/urls/

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'organiser.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', 'about.views.about'),
    # url(r'^$', direct_to_template, {"template": "about/about.html"}, name="about"),
    url(r'^about/support$', 'about.views.support'),
    url(r'^organiser/', include('organiser.urls')),
    url(r'^test/$', 'organiser.views.test_json'),
]
