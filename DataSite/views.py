from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("hello world!")
    return render(request, "index.html",)


def login(request):
    return render(request, "login.html",)


def register(request):
    return render(request, "register.html",)


def tables(request):
    return render(request, "tables.html",)


def charts(request):
    return render(request, "charts.html",)


def check(request):
    return render(request, "check.html",)


def forms(request):
    return render(request, "forms.html",)

