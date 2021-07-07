from django.shortcuts import render
from .models import registrationpage

# Create your views here.

def home(request):
    reginfo=registrationpage.objects.all()
    user={"reg" :reginfo}
    return render(request,'registration/registration.html',user)
