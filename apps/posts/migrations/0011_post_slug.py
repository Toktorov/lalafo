# Generated by Django 4.0.5 on 2022-07-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Человекопонятный URL (само генерация)'),
        ),
    ]
