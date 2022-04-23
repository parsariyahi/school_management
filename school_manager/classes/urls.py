from django.urls import path
from .views import (
    index
)
app_name = 'class'

urlpatterns = [
    path('', index, name='index'),
]
