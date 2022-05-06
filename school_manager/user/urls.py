from django.urls import path, include

from .views import (
    index,
    student_login, student_register,
    teacher_login, teacher_register,
)

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/student', student_login, name='student_login'),
    path('accounts/login/teacher', teacher_login, name='teacher_login'),
    path('accounts/register/student', student_register, name='student_register'),
    path('accounts/register/teacher', teacher_register, name='teacher_register'),
]
