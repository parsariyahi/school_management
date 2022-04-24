from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Book

MAIN_TEMPLATE_DIR = 'book'

def index(request) :
    """Main page of book app,

    :context
        :books [has all books from database]
    :return
        :render 'book/index.html
    """
    template_name = f'{MAIN_TEMPLATE_DIR}/index.html'
    books = Book.objects.all()
    
    context = {
        'books': books,
    }

    return render(request, template_name, context)