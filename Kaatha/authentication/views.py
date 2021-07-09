from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def authlogin(request):
    if request.method=="POST":
        uu=request.POST.get('user')
        pp=request.POST.get('password')

        userinfo=authenticate(request,username=uu,password=pp)
        if userinfo is not None:
            login(request,userinfo)
            return redirect('login.profile')

        else:
            messages.error(request, 'Ivalid User or Password!')

    return render(request,'authentication/login.html')


def profile(request):
    return render(request,'authentication/profile.html')



def registration(request):
    if request.method=="POST":
        un=request.POST['user']
        em=request.POST['email']
        pwd=request.POST['password']

        if User.objects.filter(username=un).exists():
            messages.warning(request, 'This user already exists!')
        else:
            userinformation=User.objects.create(username=un,email=em,password=pwd)
            userinformation.save()
            return redirect('login.registration')



    return render(request,'authentication/registration.html')






def userlogout(request):
    logout(request)
    return redirect('login')

   