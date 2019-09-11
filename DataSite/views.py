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
    if request.method == 'GET':
        return render(request, 'check.html')
    elif request.method == 'POST':
        obj = request.FILES.get('fileInputed')
        # f = open(os.path.join('uploadFiles', obj.name), 'wb')
        f = open('F:\\UPLOADFILE\\' + obj.name, 'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
        # return HttpResponse('上传成功')
        return render(request, "check.html", {"data": "上传成功"})


def forms(request):
    return render(request, "forms.html",)

