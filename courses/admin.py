from django.contrib import admin
from .models import Course, Lesson, Video
from embed_video.admin import AdminVideoMixin

# Register your models here.
admin.site.register([Course, Lesson, Video])
