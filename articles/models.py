from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to="articles/")
    slug = models.SlugField(max_length=100,unique=True)
    article_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-article_date', )