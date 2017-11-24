from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Hello, I am the main app.  You should check out our blog!"
    return HttpResponse(response)

