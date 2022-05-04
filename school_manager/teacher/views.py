from django.shortcuts import render

from django.shortcuts import render

from .models import Teacher

MAIN_TEMPLATE_DIR = 'teacher'

def index(request) :
    """Main page of Teacher app,

    :context
        :teachers [has all Teachers from database]
    :return
        :render 'teacher/index.html
    """
    template_name = f'{MAIN_TEMPLATE_DIR}/index.html'
    teachers = Teacher.objects.all()
    
    context = {
        'teachers': teachers,
    }

    return render(request, template_name, context)


def detail(request, teacher_id) :
    """Detail of each Teacher,
    
    :param teacher_id [Type: int]

    :context
        :student [has the requested Teacher detail]
        :classes [has the requested Teacher classes]
    :return
        :render 'teacher/detail.html'
    """
    template_name = f'{MAIN_TEMPLATE_DIR}/detail.html'
    teacher = Teacher.objects.get(id=teacher_id)
    classes = teacher.class_set.all()

    context = {
        'teacher': teacher,
        'classes': classes,
    }

    return render(request, template_name, context)
