from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to display ALL blogs!"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, blog):
    return HttpResponse("Placeholder to display blog " + blog)

def edit(request, blog):
    return HttpResponse("Placeholder to edit blog " + blog)

def destroy(request, blog):
    return redirect('/blogs')

