# Generated by Django 4.1.7 on 2023-03-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
