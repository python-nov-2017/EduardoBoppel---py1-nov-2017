from django.shortcuts import render, redirect, HttpResponse
from django.forms import modelform_factory
from django.core.urlresolvers import reverse
from models import *

########### COURSES
def index(request):    
    return render(request, 'courses/index.html', {'courses': Course.objects.all() })

def addcourse(request):
    form = CourseForm()
    return render(request, 'courses/newcourse.html', {'form': form } )

def createcourse(request, id=None):
    if id:
        course = Course.objects.get(id=id)
        form = CourseForm(request.POST, instance=course)
    else:
        form = CourseForm(request.POST)
    
    if form.is_valid():
        form.save(id)
        return redirect(reverse('courses:index'))
    else:
        print "error"
        return redirect(reverse('courses:addcourse'))


def editcourse(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance = course)
    return render(request,'courses/newcourse.html', {'form': form, 'id': course.id })


def deletecourse(request, id):
    Course.objects.get(id=id).delete()
    return redirect(reverse('courses:index'))


def showcomments(request, id): 
    course = Course.objects.get(id=id)
    comments = Comment.objects.filter(course=course)
    return render(request, 'courses/comments.html', {'comments': comments, 'id': id})

def addcomment(request, id):
    user = User.objects.first()
    course = Course.objects.get(id=id)
    comment = Comment.objects.create(user=user, course=course, comment=request.POST['comment'])
    comment.save()    
    return redirect(reverse('courses:showcomments', kwargs={'id': id }))
