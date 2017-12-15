from django.shortcuts import render, redirect, HttpResponse
from .models import Note

def index(request):
    return render(request, 'ajaxpost/index.html', {'notes': Note.objects.all() })

def addnote(request):
    note = Note.objects.create(note=request.POST['newnote'])
    return HttpResponse('<div class="col-6 col-sm-3">{}</div>'.format(note.note))
    
    