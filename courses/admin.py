from django.contrib import admin
from .models import Course, Lesson

# Register your models here.
admin.site.register([Course, Lesson])