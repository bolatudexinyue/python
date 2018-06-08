from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from rock.models import userinfo  ,movies ,collected


def Home(request):

    mv = movies.objects.all()
    return render(request,'rock/home.html',{'movi':mv})
def Home_logined(request):
    username = request.session.get("username")
    data = {
        "username": username
    }
    mv = movies.objects.all()
    userid = userinfo.objects.filter(username=username).first().id
    cid = collected.objects.filter(user_list_id=userid).all()
    list_m = []
    for i in cid:
        print(i.movie_list_id)
        mid = i.movie_list_id
        list_m.append(mid)

    for j in mv:
        print(j.id)
    return render(request,'rock/home_logined.html',{"data":data,'movi':mv,'list':list_m})
def Home_logined_collected(request):
    username = request.session.get("username")
    uata = {
        "username": username
    }
    mata = movies.objects.all()
    userid = userinfo.objects.filter(username=username).first().id
    cid = collected.objects.filter(user_list_id=userid).all()
    list_m = []
    for i in cid:
        print(i.movie_list_id)
        mid = i.movie_list_id
        list_m.append(mid)
    return render(request,'rock/home_logined_collected.html',{'data':list_m,"mata":mata,'uata':uata})
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        userobj = userinfo.objects.filter(username=username).first()
        passwd = userobj.password

        print(userobj,username,password)

        if userobj:
            if password == passwd:
             request.session['username'] = username
            return redirect('/rock/home_logined/')
        else:
            return render(request, 'rock/login.html')
    return render(request,'rock/login.html')
def Register(request):
    if request.method=="POST":
        from rock.models import userinfo
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        userobj = userinfo.objects.filter(username=username)
        if userobj:
            return HttpResponse("用户已存在")
        else:
            if password !=password1:
                return HttpResponse("密码输入有误")
            userinfo.objects.create(
                username=username,
                password=password,
                email=email,
            )
            return render(request,'rock/login.html')
    return render(request,'rock/register.html')
def Userinfo_mod(request):
    if request.method == "GET":

        account = request.session.get("username")
        userobj = userinfo.objects.filter(username=account).values('username','email')
        return render(request, 'rock/userinfo_mod.html', {"data": userobj})
    if request.method == "POST":
        account = request.session.get("username")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        userinfo.objects.filter(username=account).update(username=username,password=password,email=email)
        return HttpResponseRedirect(reverse('rock:home'))

def Collected(request):
    mid = request.POST.get('pk')
    account = request.session.get('username')
    uid = userinfo.objects.filter(username=account).first()
    collected.objects.create(
        movie_list_id=mid,
        user_list=uid
    )
    return HttpResponseRedirect(reverse('rock:home_logined_collected'))


def delCollected(request):
    mid = request.POST.get('pk')
    account = request.session.get('username')
    uid = userinfo.objects.filter(username=account).first()
    collected.objects.filter(movie_list=mid,user_list=uid).delete()
    return HttpResponseRedirect(reverse('rock:home_logined_collected'))