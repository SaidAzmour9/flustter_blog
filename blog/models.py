from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BlogInfo(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

class Privacy(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

class Terms(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

class Support(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

class About(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

