from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

def image_upload(instance, filename):
    imagename , extention = filename.split(".")
    return "articles/%s.%s"%(instance.id,extention)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(max_length=100,unique=True)
    article_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-article_date', )