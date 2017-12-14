from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = 'home/index.html'

