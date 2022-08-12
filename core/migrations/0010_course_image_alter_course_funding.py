# Generated by Django 4.0.3 on 2022-07-06 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_research_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='funding',
            field=models.TextField(),
        ),
    ]
