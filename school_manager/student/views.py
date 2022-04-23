from django.shortcuts import render, HttpResponse
from django.views import View


def index(request) :
    return HttpResponse('student')