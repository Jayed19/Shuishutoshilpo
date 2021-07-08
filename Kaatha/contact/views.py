from django.shortcuts import render
from .models import contact

# Create your views here.

def contactus(request):
    if request.method=="POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        p=request.POST.get('phone')
        m=request.POST.get('msg')

        contactdata=contact(name=n,email=e,phone=p,msg=m)
        contactdata.save()
        
    
    return render(request,'contact/contact.html')
