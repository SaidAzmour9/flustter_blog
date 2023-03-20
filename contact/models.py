from django.db import models

# Create your models here.


class Info(models.Model):
    place = models.CharField(max_length=200)
    place_2 = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'