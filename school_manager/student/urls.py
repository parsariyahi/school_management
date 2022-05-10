from django.urls import path
from .views import (
    profile,
)
app_name = 'student'

urlpatterns = [
    path('', profile, name='profile'),
]
