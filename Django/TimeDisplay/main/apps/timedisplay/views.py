from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def index(request):
    timeinfo = {
        "date": strftime("%a, %d-%b-%Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }

    return render(request,'timedisplay/index.html', timeinfo)
