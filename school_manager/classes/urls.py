from django.urls import path

from .views import (
    index,
    detail,
)

app_name = 'class'

urlpatterns = [
    path('', index, name='index'),
    path('<int:class_id>/detail/', detail, name='detail'),
]
