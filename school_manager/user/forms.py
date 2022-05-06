from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User

from student.models import Student
from teacher.models import Teacher

class StudentRegisterForm(UserCreationForm):
    national_id = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField( max_length=50)
    phone_number = forms.CharField( max_length=50)
    email = forms.EmailField( max_length=250)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'national_id', 'first_name', 'last_name',
            'phone_number', 'email',
            )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.save()
        student = Student.objects.create(user=user)

        return user

class TeacherRegisterForm(UserCreationForm):
    national_id = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField( max_length=50)
    phone_number = forms.CharField( max_length=50)
    email = forms.EmailField( max_length=250)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'national_id', 'first_name', 'last_name',
            'phone_number', 'email',
            )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 2
        user.save()
        teacher = Teacher.objects.create(user=user)

        return user
