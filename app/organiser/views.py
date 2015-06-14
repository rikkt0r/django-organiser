from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, "index.html")

def test_json(request):
    return JsonResponse({
        'test': [],
        'test2': {},
        'test3': [{}, {}, {}]
    })
