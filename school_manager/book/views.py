from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Book

def index(request) :
    template_name = 'book/index.html'
    books = Book.objects.all()
    
    context = {
        'books': books,
    }

    return render(request, template_name, context)