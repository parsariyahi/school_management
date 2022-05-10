# Generated by Django 4.0.4 on 2022-05-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_email_alter_user_national_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'school_manager')], default=1),
        ),
    ]
