from django.urls import path

from .views import (
    index,
    # fake_students,
    # fake_teachers,
    # fake_classes,
    # fake_books,
)

app_name = 'dashboard'

urlpatterns = [
    path('', index, name='index'),

    # path('fake/students', fake_students, name='fake_students'),
    # path('fake/teachers', fake_teachers, name='fake_teachers'),
    # path('fake/classes', fake_classes, name='fake_classes'),
    # path('fake/books', fake_books, name='fake_books'),
]
