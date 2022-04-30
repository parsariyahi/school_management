# Generated by Django 4.0.4 on 2022-04-30 05:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_classes'),
        ('teacher', '0001_initial'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='end_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.AddField(
            model_name='class',
            name='start_time',
            field=models.TimeField(default=datetime.time(7, 0)),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='student.student'),
        ),
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]
