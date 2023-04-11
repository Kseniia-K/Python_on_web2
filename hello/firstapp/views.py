from django.shortcuts import render
from django.http import HttpResponse

# Create your view here.

def index(request):
    return HttpResponse("Hello World! Это мой первый проект на Django!")
