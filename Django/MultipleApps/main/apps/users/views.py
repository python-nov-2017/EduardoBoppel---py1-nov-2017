from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Placeholder to later display the list of all users")

def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to login")
