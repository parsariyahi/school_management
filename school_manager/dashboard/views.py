from django.shortcuts import render

from django.shortcuts import render, HttpResponse
from django.views import View

def index(request) :
    template_name = 'dashboard/index.html'
    context = {}
    
    return render(request, template_name, context)