from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, FormView
from .models import User
from .forms import UserCreationForm



class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/registration.html'
    success_url = '/'





# FUNCTION BASED
# def index(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     else: 
#         form = UserCreationForm()

#     return render(request, 'users/index.html', {'form': form})


