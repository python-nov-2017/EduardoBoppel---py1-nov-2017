from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    return render(request, 'users/index.html', { 'users': User.objects.all() } )
    

def new(request):
    #show template with form to create a new user
        #create form
    form = UserForm()
    return render(request, 'users/new.html', {'form': form})

def create(request):
    form = UserForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        User.objects.create(email=email, first_name=first_name, last_name=last_name)
        return redirect('/')

    else:
        return redirect('users/new')


def show(request, id):
    return render(request, 'users/user.html', {'user': User.objects.get(id=id)} )


def edit(request, id):
    user = User.objects.get(id=id)
    form = UserForm(initial={ 
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'email': user.email
                            })
    return render(request, 'users/edit.html', {'form': form, 'id': id} )
    pass


def update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance=user)
    print form
    if form.is_valid():
        user.email = form.cleaned_data['email']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        return redirect('/users/{}'.format(id))
    else:
        print "error saving"
        return redirect('/users/{}/edit'.format(id))

    

    

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/')

