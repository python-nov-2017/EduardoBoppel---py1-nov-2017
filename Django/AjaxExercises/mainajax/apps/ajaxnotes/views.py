from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Im in ajax notes")