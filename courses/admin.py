from django.contrib import admin
from .models import Course, Lesson, Video
from embed_video.admin import AdminVideoMixin

class videoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
  
# Register your models here.
admin.site.register([Course, Lesson, Video])
admin.site.register(Video, videoAdmin)
