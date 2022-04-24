from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('student/', include('student.urls')),
    path('class/', include('classes.urls')),
    path('book/', include('book.urls')),
]
