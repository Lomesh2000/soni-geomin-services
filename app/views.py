from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name':'lomesh'})

def add(request):
    number1 = request.POST['number1']
    number2 = request.POST['number2']
    result = int(number1)+int(number2)
    return render(request, 'result.html', {'result':result})
