from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import json

def index(request):
    request.session.setdefault('words', [])
    print request.session['words']
    return render(request, 'session_words/index.html', request.session)


def add_word(request):
    size = request.POST.get('big', '')
    color = request.POST.get('color', '')
    newword = dict(word = request.POST['word'], color = color, size = size, created_at = datetime.now().strftime("%H:%M %p, %B %d, %Y"))

    wordslist = request.session['words']    
    wordslist.append(newword)
    request.session['words'] = wordslist
    
    return redirect('/')


def clear_session(request):
    del request.session['words']
    return redirect('/')