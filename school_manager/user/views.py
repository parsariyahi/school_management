from django.shortcuts import render
from django.http import JsonResponse

MAIN_TEMPLATE_DIR='user'

def index(request) :
    template_name = f'{MAIN_TEMPLATE_DIR}/index.html'
    context = {}
    
    return render(request, template_name, context)


def student_login(request):
    template_name = f'{MAIN_TEMPLATE_DIR}/student_login.html'
    context = {}
    
    return render(request, template_name, context)

def student_register(request):
    template_name = f'{MAIN_TEMPLATE_DIR}/student_register.html'
    context = {}
    
    return render(request, template_name, context)

def teacher_login(request):
    template_name = f'{MAIN_TEMPLATE_DIR}/teacher_login.html'
    context = {}
    
    return render(request, template_name, context)

def teacher_register(request):
    template_name = f'{MAIN_TEMPLATE_DIR}/teacher_register.html'
    context = {}
    
    return render(request, template_name, context)
