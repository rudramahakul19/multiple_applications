from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rohit(request):
    return render(request,'rohit.html')

def bumra(request):
    return HttpResponse('<h1>Best bowler</h1>')