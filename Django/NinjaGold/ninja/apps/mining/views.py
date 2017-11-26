from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

def index(request):
    return render(request, 'mining/index.html')

def process_gold(request, place):
    if place == "farm": won = random.randrange(10, 21)
    if place == "cave": won = random.randrange(5, 11)
    if place == "house": won = random.randrange(2, 6)
    if place == "casino": won = random.randrange(-51, 51)
    luck = "Earned" if won >= 0 else "Lost"

    newentry = dict(result = "{}:  {} {} golds from the {}!".format(datetime.datetime.now(), luck, won, place), luck=luck)    
    log = request.session.setdefault('log', [])
    log.insert(0, newentry)
    request.session['log'] = log


    request.session['total'] = request.session.setdefault('total', 0) + won

    
    return redirect('/')


def clear(request):
    del request.session['total']
    del request.session['log']
    return redirect('/')