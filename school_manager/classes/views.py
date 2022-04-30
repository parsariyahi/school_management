from django.shortcuts import render

from .models import Class

MAIN_TEMPLATE_DIR = 'class'

def index(request) :
    """Main page of classes app,

    :context
        :classes [has all classes from database]
    :return
        :render 'class/index.html
    """
    template_name = f'{MAIN_TEMPLATE_DIR}/index.html'
    classes = Class.objects.all()
    
    context = {
        'classes': classes,
    }

    return render(request, template_name, context)

def detail(request, class_id) :
    """Detail of each class,

    :param class_id [Type: int]

    :context
        :class [has the requested class detail]
        :students [has the requested class students]
    :return
        :render 'class/detail.html'
    """
    template_name = f'{MAIN_TEMPLATE_DIR}/detail.html'
    class_ = Class.objects.get(id=class_id) # use '_' after 'class' because 'class' is a keyword
    students = class_.students.all()

    context = {
        'class': class_,
        'students': students,
    }

    return render(request, template_name, context)
