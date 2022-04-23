from django.urls import path
from .views import (
    index
)
app_name = 'classes'

urlpatterns = [
    path('', index, name='index'),
]
