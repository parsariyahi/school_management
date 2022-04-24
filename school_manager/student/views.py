from django.shortcuts import render

from .models import Student

MAIN_TEMPLATE_DIR = 'student'

def index(request) :
    """Main page of student app,

    :context
        :students [has all students from database]
    :return
        :render 'student/index.html
    """
    template_name = f'{MAIN_TEMPLATE_DIR}/index.html'
    students = Student.objects.all()
    
    context = {
        'students': students,
    }

    return render(request, template_name, context)


def detail(request, student_id) :
    """Detail of each student,
    
    :param student_id [Type: int]

    :context
        :student [has the requested student detail]
        :classes [has the requested student classes]
    :return
        :render 'student/detail.html'
    """
    template_name = f'{MAIN_TEMPLATE_DIR}/detail.html'
    student = Student.objects.get(id=student_id)
    classes = student.classes.all()

    context = {
        'student': student,
        'classes': classes,
    }

    return render(request, template_name, context)