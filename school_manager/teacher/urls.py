from django.urls import path
from .views import (
    profile,
)
app_name = 'teacher'

urlpatterns = [
    path('', profile, name='profile'),
]
