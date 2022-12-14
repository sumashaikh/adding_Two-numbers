# I have decreated this file -sumayya
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render (request,'index.html',{'uname':'FAIZ'})
def about(request):
    return HttpResponse("hello sumayya")
def add(request):
    val1 = request.GET["num1"]
    val2 = request.GET["num2"]
    res = val1 + val2
    return render(request,'result.html',{'result':'res'})