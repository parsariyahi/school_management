from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout


MAIN_TEMPLATE_DIR='user'

def index(request) :
    template_name = f'{MAIN_TEMPLATE_DIR}/index.html'
    context = {}
    
    return render(request, template_name, context)

def logout_view(request) :
    logout(request)
    return redirect('dashboard:index')
    
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
