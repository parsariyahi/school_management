from django.db import models

"""
One to One field with 'classes'
"""

class Teacher(models.Model) :
    personal_id = models.CharField(
        max_length=50,
        unique=True,
    )

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    phone_number = models.CharField(
        max_length=50, 
        unique=True,
    )
    email = models.EmailField(
        max_length=250, 
        unique=True,
    )

