from django.contrib import admin
from .models import Course, Lesson
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = (
        ('course', admin.RelatedOnlyFieldListFilter),
    )

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Lesson, LessonAdmin)