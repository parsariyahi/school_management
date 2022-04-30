from django.shortcuts import render

from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views import View


from faker import Faker
from random import randint, choice
from datetime import time

from classes.models import Class
from student.models import Student
from teacher.models import Teacher
from book.models import Book


def index(request) :
    template_name = 'dashboard/index.html'
    context = {}
    
    return render(request, template_name, context)

def test(request) :
    faker = Faker()

    t = randint(7, 16)

    students = []
    books = []
    teachers = []
    classes = []

    for _ in range(10):
        student = {
            'national_id': faker.random_int(10000000, 99999999),
            'name': faker.first_name(),
            'last_name': faker.last_name(),
            'phone_number': '09' + str(faker.random_int(1000000000, 9999999999)),
        }
        students.append(student)

        teacher = {
            'personal_id': faker.random_int(10000000, 99999999),
            'name': faker.first_name(),
            'last_name': faker.last_name(),
            'phone_number': '09' + str(faker.random_int(1000000000, 9999999999)),
            'email': faker.first_name() + '@gmail.com',
        }
        teachers.append(teacher)

        book = {
            'name': ' '.join(faker.words(4)),
        }
        books.append(book)

        class_ = {
            'name': ' '.join(faker.words(4)),
            'start_time': time(t, 0, 0),
            'end_time': time(t+2, 0, 0),
            'book': choice(books),
            'teacher': choice(teachers),
            'students': students,
        }
        classes.append(class_)

    data = {
        's': students,
        't': teachers,
        'b': books,
        'c': classes,
    }

    return JsonResponse(data)
