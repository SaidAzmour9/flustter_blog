from django.contrib import admin
from .models import Course, Lesson
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    search_fields = ['title','course']
    list_display = ['title','course']
    list_filter = ['course']


admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)