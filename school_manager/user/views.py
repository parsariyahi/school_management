from django.shortcuts import render, redirect
from django.http import JsonResponse # just for testing
from django.contrib.auth import authenticate, login, logout

from .forms import (
    StudentRegisterForm, 
    TeacherRegisterForm,
)


MAIN_TEMPLATE_DIR='user'
# the pattern for each template is 
# f'{MAIN_TEMPLATE_DIR}/{TEMPLATE_NAME}'

def index(request) :
    template_path = f'{MAIN_TEMPLATE_DIR}/index.html'
    context = {}
    
    return render(request, template_path, context)

def logout_view(request) :
    logout(request)
    return redirect('dashboard:index')
    
def student_login(request):
    template_path = f'{MAIN_TEMPLATE_DIR}/student_login.html'
    context = {}
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            return redirect('dashboard:index')

    return render(request, template_path, context)

def student_register(request):
    template_path = f'{MAIN_TEMPLATE_DIR}/student_register.html'
    context = {}
    
    if request.method == 'POST' :
        form = StudentRegisterForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            return redirect('dashboard:index')

    else :
        form = StudentRegisterForm()
        context['form'] = form # add form to context

    return render(request, template_path, context)

def teacher_login(request):
    template_path = f'{MAIN_TEMPLATE_DIR}/teacher_login.html'
    context = {}
    
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('dashboard:index')

    return render(request, template_path, context)

def teacher_register(request):
    template_path = f'{MAIN_TEMPLATE_DIR}/teacher_register.html'
    context = {}
    
    if request.method == 'POST' :
        form = TeacherRegisterForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            return redirect('dashboard:index')

    else :
        form = TeacherRegisterForm()
        context['form'] = form # add form to context

    return render(request, template_path, context)
