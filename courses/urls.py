from blog.urls import app_name
from . import views
from django.urls import path
from .views import CourseListView, LessonDetailView, CourseDetailView

app_name = 'courses'


urlpatterns = [
    path('', CourseListView.as_view(), name="courses_list"),
    path('<str:course_slug>', CourseDetailView.as_view(), name="course_detail"),
    path('<str:course_slug>/<str:lesson_slug>', LessonDetailView.as_view(), name="lesson_detail"),
]