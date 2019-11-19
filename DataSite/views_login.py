from django.shortcuts import render
from django.shortcuts import HttpResponse
from DataSite.models import Users
import hashlib
import base64
import time
import datetime
import json
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    if request.method == 'POST':
        result = checkin(request.POST)
        if result == "登陆失败":
            return render(request, "login.html")
        else:
            return render(request, "index.html", {'data': result})


def checkin(post):
    account = post.get("loginUseraccount", None)
    password = post.get("loginPassword", None)
    a = (account + password)
    epassword = encode(a)
    q1 = Users.objects.filter(Account=account)
    q2 = q1.filter(Password=epassword)
    if q2.count() > 0:
        return q2[0]
    else:
        return "登陆失败"


def encode(s):
    b = bytes(s, encoding='gb2312')
    h = hashlib.sha512(b).digest()
    c = base64.b64encode(h)
    d = str(c, encoding='gb2312')
    return d
