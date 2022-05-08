from django.db import models
from user.models import User

"""
Many to Many field with 'classes'
"""

class Student(models.Model) :
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self) :
        return self.user.username
