# Generated by Django 4.0.5 on 2022-07-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='blog_image/')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блог',
            },
        ),
    ]
