from django.shortcuts import render

def func(request):
    return render(request,'h1.html')

def fnc(request):
    return render(request,'h2.html')
