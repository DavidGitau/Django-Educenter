# Generated by Django 4.0.3 on 2022-07-18 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_scholarship_s_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarship',
            name='s_course',
        ),
    ]
