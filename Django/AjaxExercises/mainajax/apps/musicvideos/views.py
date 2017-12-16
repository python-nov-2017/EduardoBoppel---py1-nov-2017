from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import requests

from models import *

def index(request):
    return render(request, 'musicvideos/index.html')


def get_movie(request):
    artist = request.POST['user_input'].replace('','')
    url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
    response = requests.get(url).content
    return HttpResponse(response, content_type='application/json')