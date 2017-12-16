from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from .forms import LeadCreationForm
from .models import Lead

LEADS_PER_PAGE = 5

def index(request):
    return render(request, "ajaxpagination/index.html", {'form': LeadCreationForm()} )


def add_lead(request):
    form = LeadCreationForm(request.POST)
    if form.is_valid():
        form.save() 
    print "im in add_lead"
    return redirect(reverse('ajaxpagination:index'))


def get_leads(filter=None):
    leads = Lead.objects.all()
    print filter.POST['page']

    if filter != None:
        if filter.POST['name'] != "":
            leads = leads.filter(first_name__startswith=filter.POST['name'])

        if filter.POST['from_date'] != "":
            leads = leads.filter(created_at__gt=filter.POST['from_date'])
        
        if filter.POST['to_date'] != "":
            leads = leads.filter(created_at__lt=filter.POST['to_date'])
    

    p = Paginator(leads, LEADS_PER_PAGE)    
    pages = range(p.num_pages)
    pages = [x+1 for x in pages]

    subset = p.page(filter.POST['page'])
    leads = subset.object_list

    return render(filter, 'ajaxpagination/leads.html', {'leads': leads, 'pages': pages})
    

