from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Courses(request):
    return HttpResponse('<h1>This is my home page</h1>')