from django.shortcuts import render
from .models import About,Dev

def  portfolio(request):
    info_me = About.objects.all()
    details = Dev.objects.all()
    return render(request,'website/index.html',{'about':info_me, 'details': details})


