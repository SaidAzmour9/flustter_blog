
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
def image_upload(instance, filename):
    imagename , extention = filename.split(".")
    return "courses/%s.%s"%(instance.id,extention)

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    content = RichTextField()
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(max_length=100,unique=True)
    course_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-course_date', )

class Lesson(models.Model):
    course = models.ForeignKey('Course', related_name='course', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField()
    slug = models.SlugField(max_length=100,unique=True)
    lesson_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    class Meta:
        ordering = ('lesson_date', )
    
    def get_lessons_queryset(self):
        return reverse('courses:lesson_detail', kwargs={'course_slug':self.course.slug, 'lesson_slug':self.slug})
    
    def get_absolute_url(self):
        return reverse('courses:lesson_detail', args=[str(self.course.slug), str(self.slug)])