from django.shortcuts import render
from django.views.generic.base import TemplateView


class Main(object):
    template = ''
    favorite_number = None
    least_favorite_number = None

    def get(self, request):        
        context = {
            'add': '',
            'subs': '',
            'mult': '',
            'div': ''
        }
        return render(request, self.template, context)

    def get_template(self):
        if self.template == "":
            raise ImproperlyConfigured('Template not defined')
        return self.template

    def add(num1, num2):
        return num1 + num2

    def substract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2


class Calculator(Main, TemplateView):
    template = 'calculator/index.html'
    favorite_number = 22
    least_favorite_number = 1

    add = self.add(favorite_number, least_favorite_number)
    
    # add = self.add(favorite_number, least_favorite_number)
    # sub = self.substract(favorite_number, least_favorite_number)
    # mult = self.multiply(favorite_number, least_favorite_number)
    # div = self.divide(favorite_number, least_favorite_number)
