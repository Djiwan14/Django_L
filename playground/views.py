from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# file where we create our views, view function - function that takes the request and returns response
# request handler

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Shokhrukh'})

def intro(request):
    return HttpResponse("Hey, It is me!")

def play(request):
    return HttpResponse("Playing, playing")