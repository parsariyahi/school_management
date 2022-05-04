from django.urls import path
from .views import (
    index,
    detail,
)
app_name = 'teacher'

urlpatterns = [
    path('', index, name='index'),
    path('<int:teacher_id>/detail/', detail, name='detail'),
]
