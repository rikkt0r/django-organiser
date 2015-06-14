from django.shortcuts import render

def about(request):
    return render(request, "about/about.html")

def support(request):
    return render(request, "about/support.html")
