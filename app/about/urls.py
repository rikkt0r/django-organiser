from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='about/about.html'), name='index'),
    url(r'^about/$', TemplateView.as_view(template_name='about/about.html'), name='about'),
    url(r'^agreement/$', TemplateView.as_view(template_name='about/agreement.html'), name='agreement'),
    url(r'^faq/$', TemplateView.as_view(template_name='about/faq.html'), name='faq'),
    url(r'^support/$', TemplateView.as_view(template_name='about/support.html'), name='support'),
]
