# -*- coding:utf-8 -*- 

from django.shortcuts import render
from django.http import HttpResponse


from .models import danci
# Create your views here.
def index(request):
    dancilist = danci.objects.order_by('-number')
    context = {'dancilist': dancilist}
    return render(request, 'jilu/index.html', context)

def add(request):
    addword = request.GET['word']
    if len(danci.objects.filter(name = addword)) > 0 :
        p = danci.objects.get(name = addword)  
        p.number = p.number + 1
        p.save()
        return HttpResponse("existed!")
    else:
        p = danci(name=addword, number=1)
        p.save()
        return HttpResponse("created!")

