from django.conf.global_settings import LOGIN_URL
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

"""
USER_TYPES:
    1 -> student,
    2 -> teacher,
"""

LOGIN_URL = 'dashboard:index'


def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    """ Decorator for views that checks that the logged in user is a student,

    redirects to the log-in page if necessary.
    """
    wrapper = user_passes_test(
        lambda u: 
        u.is_active and u.user_type == 1,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return wrapper(function)
    return wrapper


def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    """ Decorator for views that checks that the logged in user is a teacher,

    redirects to the log-in page if necessary.
    """
    wrapper = user_passes_test(
        lambda u: 
        u.is_active and u.user_type == 2,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return wrapper(function)
    return wrapper
