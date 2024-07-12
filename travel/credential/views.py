from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages,auth

def login(request):
    if request.method == 'POST':
        us = request.POST['usernamel']
        pa = request.POST['passwordl']
        user=auth.authenticate(username=us,password=pa)
        if user is not None:
                 auth.login(request,user)
                 return redirect('/')
        else:
              messages.info(request,"invalid user")
              return  redirect('login')
    return render(request, "login.html")
def register(request):
     if request.method == 'POST':
        u=request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        e = request.POST['email']
        p = request.POST['password']
        cf = request.POST['password1']
        if p==cf:
            if User.objects.filter(username=u).exists():
                           messages.info(request,"username already exist")
                           return redirect('register')
            elif User.objects.filter(email=e).exists():
                           messages.info(request,"email already exist")
                           return redirect('register')
            else:
                user = User.objects.create_user(username=u,first_name=fn,last_name=ln,email=e,
                                        password=p)
                user.save()
                return redirect('login')
        else:
              messages.info(request,"passwords does not match")
              return redirect('register')
        return redirect('/')
     return render(request,"registeration.html")
def logout(request):
    auth.logout(request)
    return redirect('/')