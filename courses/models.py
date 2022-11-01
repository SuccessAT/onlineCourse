from django.db import models
from accounts.models import Student, Teacher
#from embed_video.fields import EmbedVideoField

# Create your models here.
class Course (models.Model):
    title = models.CharField (max_length=150)
    description = models.CharField(max_length=250, default="No Description")
    student = models.ManyToManyField(Student, related_name='courses', blank=True)
    teacher = models.ManyToManyField(Teacher, related_name='teacher', blank=True)

    def __str__(self):
        return self.title

class Lesson (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="No Description")
    video = models.URLField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    
    class  Meta:
        verbose_name_plural = "Lesson"

    def __str__(self):
        return self.title

'''class Video (models.Model):
    title = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField(default="https://www.youtube.com/embed/P408kZDci0A")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='videos')
	
    class  Meta:
        verbose_name_plural = "Video"
	
    def __str__(self):
        return str(self.lesson.title)'''
