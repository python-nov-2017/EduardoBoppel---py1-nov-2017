from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("Placeholder to see all surveys created")

def new(request):
    return HttpResponse("Placeholder for users to add a new survey")
    




