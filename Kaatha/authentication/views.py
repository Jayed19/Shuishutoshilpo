from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def authlogin(request):
    if request.method=="POST":
        uname=request.POST.get('user')
        pwrd=request.POST.get('password')

        userinfo=authenticate(request,username=uname,password=pwrd)
        if userinfo is not None:
            login(request,userinfo)
            return redirect('/contact')

        else:
            print("invalid user or password")

    return render(request,'authentication/login.html')

def registration(request):
    return render(request,'authentication/registration.html')