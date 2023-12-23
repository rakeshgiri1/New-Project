from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse("Hello, Django!")

def learn_python(request):
    return HttpResponse("Hello Pyhon!")

def learn_math(request):
    return HttpResponse("20!")

def learn_var(request):
    num = 20+20
    return HttpResponse(num)

def learn_format(request):
    a='Rakesh Giri'
    return HttpResponse("My name is {}".format(a))

































