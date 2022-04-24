from django.urls import path
from .views import (
    index
)

app_name = 'book'

urlpatterns = [
    path('', index, name='index'),
]
