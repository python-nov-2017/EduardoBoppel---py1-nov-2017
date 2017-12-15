from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import Note

def index(request):
    return render(request, "ajaxnotes/index.html", {'notes': Note.objects.all()} )

def add_note(request):
    return render(request, 'ajaxnotes/new_note.html', {'note': Note.objects.create(title=request.POST['note_title'])})
    
def add_description(request, id):
    note = Note.objects.get(id=id)
    note.description = request.POST['note_description']
    note.save()
    return JsonResponse({
        'id': id,
        'description': note.description
    })

def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return JsonResponse(id, safe=False)