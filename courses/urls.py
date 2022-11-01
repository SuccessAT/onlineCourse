
from django.urls import path
from .views import CoursesListView, CoursesDetailView, LessonView, VideoView, CourseDetailDeleteView, CourseCreateView, AboutUsView

urlpatterns = [
    path('', CoursesListView.as_view(), name='courses'),
    path('<int:pk>', CourseDetailDeleteView.as_view(), name='course_detail'),
    path('create', CourseCreateView.as_view(), name='course_create'),
    #path('<int:pk>/edit', CourseDetailDeleteView.as_view(), name='course_edit'),
    path('lesson/<int:pk>', LessonView.as_view(), name = 'lesson'),
    #path('video/<int:pk>', VideoView.as_view(), name = 'video'),
    path('aboutus', AboutUsView.as_view(), name='aboutus')
    #path('enrollment', EnrollmentOnCourseView.as_view(), name='enrollment'),

]
