from django.views.generic import TemplateView

class Template404View(TemplateView):
    template_name = "error_404.html"

class Template500View(TemplateView):
    template_name = "error_500.html"
