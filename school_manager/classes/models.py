from datetime import time

from django.db import models

from book.models import Book
from teacher.models import Teacher
from student.models import Student

DEFAULT_START_TIME = time(7, 0, 0)
DEFAULT_END_TIME = time(9, 0, 0)

class Class(models.Model):
    name = models.CharField(max_length=50)

    start_time = models.TimeField(
        auto_now=False, 
        auto_now_add=False,
        default=DEFAULT_START_TIME,
    )
    end_time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        default=DEFAULT_END_TIME,
    )

    # Relations
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE,
    )
    teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.CASCADE
    )
    students = models.ManyToManyField(
        Student,
        related_name='class_students',
    )
