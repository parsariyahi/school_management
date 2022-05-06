from django.db import models
from user.models import User

"""
One to One field with 'classes'
"""

class Teacher(models.Model) :
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )