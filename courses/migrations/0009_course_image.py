# Generated by Django 4.1.7 on 2023-03-16 18:35

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_course_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to=courses.models.image_upload),
            preserve_default=False,
        ),
    ]
