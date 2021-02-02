from django.shortcuts import render
import datetime as time
from django.http import HttpResponse

def currentdate(request):
    response="<html><body>it is now %s</body></html>" %time.datetime.now()
    return HttpResponse(response)

# Create your views here.o
def getall(request):
    data=input("Enter Your name")
    return HttpResponse("Hi %s" %data)


def hoursahead(request,offset):
    offset=int(offset)
    dt = time.datetime.now() + time.timedelta(hours=offset)
    response="<html><body>it is now %s</body></html>" %dt
    return HttpResponse(response)
def getname(request,name):
    return HttpResponse(name)