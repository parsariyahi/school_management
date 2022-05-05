from django.shortcuts import render
from django.http import JsonResponse

"""Uncomment these lines,

if you want to use fake data views
"""
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


def fake_teachers(request) :
    """Uncomment these lines,

    if you want to use fake data views
    """
    # faker = Faker()

    # Fake Teachers
    # for _ in range(10) :
    #     name = faker.first_name()
    #     teacher = {
    #         'personal_id': faker.random_int(10000000, 99999999),
    #         'name': 'mr.' + name,
    #         'last_name': faker.last_name(),
    #         'phone_number': '09' + str(faker.random_int(1000000000, 9999999999)),
    #         'email': name + '@gmail.com',
    #     }
    #     t = Teacher(**teacher)
    #     t.save()
    return JsonResponse({'status': 'true'})

def fake_students(request) :
    """Uncomment these lines,

    if you want to use fake data views
    """
    # faker = Faker()

    # Fake Students
    # for _ in range(50):
    #     student = {
    #         'national_id': faker.random_int(10000000, 99999999),
    #         'name': faker.first_name(),
    #         'last_name': faker.last_name(),
    #         'phone_number': '09' + str(faker.random_int(1000000000, 9999999999)),
    #     }
    #     s = Student(**student)
    #     s.save()
    return JsonResponse({'status': 'true'})

def fake_classes(request) :
    """Uncomment these lines,

    if you want to use fake data views
    """
    # faker = Faker()

    # Fake Classes
    # books = Book.objects.all()
    # teachers = Teacher.objects.all()
    #
    #
    # for _ in range(10) :
    #     b = randint(1, 9) # b: book
    #     t = randint(1, 9) # t: teacher
    #     class_time = randint(7, 16)
    #
    #     class_ = {
    #         'name': ' '.join(faker.words(4)),
    #         'start_time': time(class_time, 0, 0),
    #         'end_time': time(class_time, 0, 0),
    #         'book': books[b],
    #         'teacher': teachers[t],
    #     }
    #     c = Class(**class_)
    #     c.save()
    #
    #     """ Set a random range of students """
    #     s = randint(1, 10)
    #     e = randint(11, 30)
    #     students = Student.objects.all()[s:e]
    #     c.students.set(students)
    return JsonResponse({'status': 'true'})

def fake_books(request) :
    """Uncomment these lines,

    if you want to use fake data views
    """
    # faker = Faker()

    # Fake Books
    # for _ in range(20) :
    #     book = {
    #         'name': ' '.join(faker.words(4)),
    #     }
    #     b = Book(**book)
    #     b.save()
    return JsonResponse({'status': 'true'})
