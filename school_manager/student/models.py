from django.db import models
# Create your models here.

from classes.models import Class

class Student(models.Model) :
    national_id = models.CharField(max_length=50, unique=True) #this is unique for each student

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    classes = models.ManyToManyField(Class)

