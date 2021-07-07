from django.shortcuts import render

# Create your views here.

def home(request):
    user={
        "name": "Jayed Ibrahim",
        "mobile":"01917858019",
        "email":"jayed19@gmail.com"
    }
    return render(request,'registration/registration.html',user)
