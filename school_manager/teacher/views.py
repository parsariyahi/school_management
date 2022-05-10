from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Teacher

MAIN_TEMPLATE_DIR = 'teacher'

@login_required
def profile(request) :
    """Teacher Profile View

    :context
        :students [has all students from database]
    :return
        :render 'student/index.html
    """
    template_name = f'{MAIN_TEMPLATE_DIR}/index.html'
    return JsonResponse({'some': 'teacher Profile'})
