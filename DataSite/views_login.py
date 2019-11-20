from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import hashlib
import base64
from rbac.models import UserInfo
from rbac.service.init_permission import init_permission
import time
import datetime
import json
# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('loginUseraccount')
        password = request.POST.get('loginPassword')
        user_obj = UserInfo.objects.filter(username=username, password=password).first()
        if not user_obj:
            return render(request, "login.html", {'error': '用户名或密码错误！'})
        else:
            init_permission(request, user_obj)  # 调用init_permission，初始化权限
            return redirect('/index/')



def getDepartment(pUser):
    try:
        departmentset = pUser.departments_set.all()
        rtDep = "";
        for fDep in departmentset:
            rtDep = rtDep + " " + fDep.Name
    except:
        rtDep = " "
    return rtDep


def encode(s):
    b = bytes(s, encoding='gb2312')
    h = hashlib.sha512(b).digest()
    c = base64.b64encode(h)
    d = str(c, encoding='gb2312')
    return d
