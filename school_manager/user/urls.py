from django.urls import path, include

from .views import (
    index, logout_view,
    student_login, student_register,
    teacher_login, teacher_register,
)

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),

    path('logout/', logout_view, name='logout'),
    path('login/student', student_login, name='student_login'),
    path('login/teacher', teacher_login, name='teacher_login'),
    path('register/student', student_register, name='student_register'),
    path('register/teacher', teacher_register, name='teacher_register'),
]
