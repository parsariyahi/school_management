from django.urls import path
from .views import (
    index,
    detail,
)
app_name = 'student'

urlpatterns = [
    path('', index, name='index'),
    path('<int:student_id>/detail/', detail, name='detail'),
]
