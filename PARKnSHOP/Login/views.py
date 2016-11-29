#--*-- coding=utf-8 --*---

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from models import Person
# Create your views here.
#注册
def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html',{})
    elif request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password =  request.POST.get('password', '')
        description = request.POST.get('description', '')
        address = request.POST.get('address', '')
        Person.objects.create(name=name,email= email,password=password,description=description,address=address)
        return HttpResponse('regist success!!')
    else:
        return HttpResponse("你到了什么不该到的地方")
   
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html',{})
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        password =  request.POST.get('password', '')
        personquery = Person.objects.filter(email__exact = email,password__exact = password)
        if personquery:
            #比较成功，跳转index
            person=Person.objects.get(email=email,password=password)
            response = HttpResponseRedirect('/login/index')
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie('pkey',person.pkey,3600)
            return response
        else:
            return HttpResponse("post完你到了什么不该到的地方")
    else:
        return HttpResponse("你到了什么不该到的地方")

#登陆成功
def index(request):
    pkey = request.COOKIES.get('pkey','')
    return render_to_response('index.html' ,{'pkey':pkey})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('pkey')
    return response

