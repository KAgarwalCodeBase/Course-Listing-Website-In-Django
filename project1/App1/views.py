from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Courses(request):
    return HttpResponse('<h1>This is my home page</h1>')
def detail(request,couse_id):
    return HttpResponse('<h2>These are the course details course id is: '+str(couse_id)+'</h2>')