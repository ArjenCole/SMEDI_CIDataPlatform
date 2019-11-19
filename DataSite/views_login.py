from django.shortcuts import render
from django.shortcuts import HttpResponse
import hashlib
import base64
import time
import datetime
import json
# Create your views here.


def login(request):
    return render(request, 'login.html', {'error': "账号密码错误！"}, )


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
