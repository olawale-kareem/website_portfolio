from django.shortcuts import render
from .models import About

def  portfolio(request):
    info_me = About.objects.all()
    return render(request,'website/index.html',{'about':info_me})


