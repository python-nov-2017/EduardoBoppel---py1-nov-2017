from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'surveys/index.html')

def process_survey(request):
    request.session['attempts'] = request.session.setdefault('attempts', 0) + 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect(reverse('surveys:results'))

def results(request):
    return render(request, 'surveys/results.html')