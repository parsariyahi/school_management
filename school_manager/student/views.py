from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Student

def index(request) :
    template_name = 'student/index.html'
    students = Student.objects.all()
    
    context = {
        'students': students,
    }

    return render(request, template_name, context)