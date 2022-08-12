# Generated by Django 4.0.3 on 2022-07-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_blog_image_remove_course_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images/blog'),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='images/courses'),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='images/events'),
        ),
        migrations.AddField(
            model_name='research',
            name='image',
            field=models.ImageField(null=True, upload_to='images/research'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='image',
            field=models.ImageField(null=True, upload_to='images/scholarship'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(null=True, upload_to='images/teachers'),
        ),
    ]
