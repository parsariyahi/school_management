from django.db import models

"""
Many to Many field with 'classes'
"""

class Student(models.Model) :
    national_id = models.CharField(
        max_length=50,
        unique=True,
    )

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
