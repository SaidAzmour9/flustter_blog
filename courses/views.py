from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from .models import Course, Lesson
from django.views.generic import ListView, DetailView

# Create your views here.

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name='courses/courses.html'


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    l_courses: Course.objects.all()[0:3]
    template_name='courses/course.html'

    def get_object(self, queryset=None):
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        return course
    




class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = 'lesson'
    template_name='courses/lesson.html'
    
    def get_object(self, queryset=None):
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        lesson = get_object_or_404(Lesson, course=course, slug=self.kwargs['lesson_slug'])
        return lesson
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        lessons = Lesson.objects.filter(course=course)
        context['course'] = course
        context['lessons'] = lessons

        lesson = self.object
    
        # Get the next and previous lessons based on their primary key (pk)
        next_lesson = Lesson.objects.filter(course=course, pk__gt=lesson.pk).order_by('pk').first()
        prev_lesson = Lesson.objects.filter(course=course, pk__lt=lesson.pk).order_by('-pk').first()

        # Add the next and previous lesson URLs to the context
        if next_lesson:
            context['next_lesson_url'] = next_lesson.get_absolute_url()

        if prev_lesson:
            context['prev_lesson_url'] = prev_lesson.get_absolute_url()

        return context

    def get_lessons_queryset(self):
        course_slug = self.kwargs.get('course_slug')
        course = Course.objects.get(slug=course_slug)
        return Lesson.objects.filter(course=course)

