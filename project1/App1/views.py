from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models  import Allcourses
from django.template import loader

# Create your views here.
def Courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('App1/Courses.html')
    context = {
        'ac':ac,
    }
    return HttpResponse(template.render(context,request))


def detail(request,couse_id):
    page = None
    try:
        course = Allcourses.objects.get(pk=couse_id)
        page = render(request, 'App1/details.html', {'course': course})
    except Allcourses.DoesNotExist:
        # raise Http404("Course Not Available")
        page =  render(request,'App1/404.html')
    return page
