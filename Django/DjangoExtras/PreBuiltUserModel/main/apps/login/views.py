from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm


def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            userlogin(request, user)
            return redirect(reverse('loginapp:home'))
        else:
            loginform = AuthenticationForm(request.POST)        
    else:
        loginform = AuthenticationForm()
    
    return render(request, 'login/login.html', {'login': loginform })

    

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)  BASIC USER CREATION FORM
        form = SignUpForm(request.POST)          #EXTENDED USER CREATION FORM
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            userlogin(request, user)
            return redirect(reverse('loginapp:home'))

    else:
        form = SignUpForm()

    return render(request, 'login/register.html', {'form': form })


@login_required
def logout(request):
    userlogout(request)
    return redirect(reverse('loginapp:index'))


@login_required
def home(request):
    allusers = User.objects.all()
    return render(request, 'login/home.html', {'allusers': allusers})
