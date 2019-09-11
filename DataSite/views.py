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
        if obj is None:
            checkList = ['未选择校验文件']
            return render(request, "check.html", {"checkList": checkList})
        else:
            # f = open(os.path.join('uploadFiles', obj.name), 'wb')
            f = open('F:\\UPLOADFILE\\' + obj.name, 'wb')
            for line in obj.chunks():
                f.write(line)
            f.close()
            checkList = ['physics', 'chemistry', 1997, 2000]
            return render(request, "check.html", {"checkList": checkList})


def forms(request):
    return render(request, "forms.html",)

