from django.shortcuts import render,get_object_or_404
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
    course = get_object_or_404(Allcourses,pk = couse_id)
    return render(request,'App1/details.html',{'course':course})
    # page = None
    # try:
    #     course = Allcourses.objects.get(pk=couse_id)
    #     page = render(request, 'App1/details.html', {'course': course})
    # except Allcourses.DoesNotExist:
    #     page =  render(request,'App1/404.html')
    # return page

def yourchoice(request, couse_id):
    course = get_object_or_404(Allcourses, pk = couse_id)
    try:
        selected_ct = course.details_set.get(pk = request.POST['choice'])
    except (KeyError,Allcourses.DoesNotExist):
        return render(request,'App1/details.html',{'course':course,'error_message':"Select a valid option"})
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        return render(request,'App1/details.html',{'course':course})

