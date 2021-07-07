from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def regular(request):
    return render(request,'regular/regular.html')
