from django.shortcuts import render, redirect, HttpResponse
from django.forms import modelform_factory
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
        return redirect('/')
    else:
        print "error"
        return redirect('/addcourse')


def editcourse(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance = course)
    return render(request,'courses/newcourse.html', {'form': form, 'id': course.id })


def deletecourse(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')


def showcomments(request, id): 
    course = Course.objects.get(id=id)
    comments = Comment.objects.filter(course=course)
    print comments
    
    return render(request, 'courses/comments.html', {'comments': comments, 'id': id})

def addcomment(request, id):
    user = User.objects.first()
    course = Course.objects.get(id=id)
    comment = Comment.objects.create(user=user, course=course, comment=request.POST['comment'])
    comment.save()    
    return redirect('/{}/showcomments'.format(id))



########### USERS
def users(request):
    return render(request, 'courses/users.html', {'users': User.objects.all() } )

def adduser(request):
    form = UserForm()
    return render(request, 'courses/newuser.html', {'form': form} )

def updateuser(request, id=None):
    if id:
        user = User.objects.get(id=id)
        form = UserForm(request.POST, instance=user)
    else: 
        form = UserForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/users')
    else:
        print "errors"
        return redirect('/users/adduser')

def showuser(request, id):
    return render(request, 'courses/showuser.html', {'user':User.objects.get(id=id) })

def edituser(request, id):
    user = User.objects.get(id=id)
    form = UserForm(instance=user)
    return render(request, 'courses/newuser.html', {'form': form, 'id': user.id} )

def deleteuser(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')