# Generated by Django 4.0.3 on 2022-07-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course_image_alter_course_funding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='images/courses'),
        ),
    ]
