from django.shortcuts import render

# Create your views here.

def home(request):
    user={
        "name": "Jayed Ibrahim",
        "mobile":"01917858019",
        "email":"jayed19@gmail.com",
        "orderList":["RK001","GJ005","BD001"]
    }
    return render(request,'registration/registration.html',user)
