#i have created the file
from django.http import HttpResponse
from django.shortcuts import render
from automation.models import Automation
from django.db.models import Q
def company(request):

    return HttpResponse("hello <br>  <a href='http://127.0.0.1/automation'> facebook </a>")
def about(request):
    return HttpResponse("Roshan <br>   <a href='/'> back</a>")
def index(request):
    prams={'name':'roshan','place' :'jharkhand'}
    return render(request,'index.html',prams)
def Upload(request):
    if request.method == 'GET':
        query= request.FILES.getlist('q')

        upload= request.GET.get('Upload')

    return render(request, 'admin/change_form.html',locals())


def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            #lookups= Q(Automation_Status=query) | Q(Team_Name=query)
            lookups = Q(Use_Case__icontains=query) | Q(Automation_Status__icontains=query)

            results= Automation.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'admin/index.html', context)

        else:
            return render(request, 'admin/index.html')

    else:
        return render(request, 'admin/index.html')
