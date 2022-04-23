from django.db import models

from book.models import Book

# Create your models here.

class Class(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)