from django.shortcuts import render

from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views import View


# from faker import Faker
# from random import randint, choice, choices
# from datetime import time

# from classes.models import Class
# from student.models import Student
# from teacher.models import Teacher
# from book.models import Book


def index(request) :
    template_name = 'dashboard/index.html'
    context = {}
    
    return render(request, template_name, context)

def test(request) :
    # faker = Faker()

    # t = randint(7, 16)

    # students = Student.objects.all()[15:40]
    # books = Book.objects.all()
    # teachers = Teacher.objects.all()
    # for _ in range(50):
    #     student = {
    #         'national_id': faker.random_int(10000000, 99999999),
    #         'name': faker.first_name(),
    #         'last_name': faker.last_name(),
    #         'phone_number': '09' + str(faker.random_int(1000000000, 9999999999)),
    #     }
    #     s = Student(**student)
    #     s.save()
    #     students.append(s)
    # for _ in range(10) :
    #     teacher = {
    #         'personal_id': faker.random_int(10000000, 99999999),
    #         'name': faker.first_name(),
    #         'last_name': faker.last_name(),
    #         'phone_number': '09' + str(faker.random_int(1000000000, 9999999999)),
    #         'email': faker.first_name() + '@gmail.com',
    #     }
    #     t = Teacher(**teacher)
    #     t.save()
    #     teachers.append(teacher)
    # for _ in range(20) :
    #     book = {
    #         'name': ' '.join(faker.words(4)),
    #     }
    #     b = Book(**book)
    #     b.save()
    #     books.append(book)
    # r = randint(1, 10)
    # for _ in range(4) :
    #     class_ = {
    #         'name': ' '.join(faker.words(4)),
    #         'start_time': time(t, 0, 0),
    #         'end_time': time(t+2, 0, 0),
    #         'book': books[8],
    #         'teacher': teachers[2],
    #     }
    #     c = Class(**class_)
    #     c.save()
        # c.students.set(students)
    # data = {
    #     's': students,
    #     't': teachers,
    #     'b': books,
    #     'c': classes,
    # }

    return JsonResponse({'somm': 'dsfasfdsf'})
