from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Class

def index(request) :
    template_name = 'class/index.html'
    classes = Class.objects.all()
    
    context = {
        'classes': classes,
    }

    return render(request, template_name, context)