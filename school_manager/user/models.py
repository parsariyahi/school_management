from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE = (
        (1, 'student'),
        (2, 'teacher'),
        (3, 'school_staff'),
    )

    national_id = models.CharField(
        max_length=50,
        unique=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=50, 
        unique=True,
    )
    email = models.EmailField(
        max_length=250, 
        unique=True,
    )
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE,
        default=1,
    )
