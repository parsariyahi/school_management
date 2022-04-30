from django.db import models

"""
One to One field with 'classes'
"""

class Book(models.Model):
    name = models.CharField(max_length=50)
