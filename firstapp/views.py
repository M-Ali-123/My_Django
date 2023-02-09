from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('HOME PAGE <a href="/about">about</a>')

def about(request):
    return HttpResponse('ABOUT PAGE <a href="/">Home</a>')