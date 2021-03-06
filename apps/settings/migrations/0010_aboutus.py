# Generated by Django 4.0.5 on 2022-07-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_alter_setting_facebook_alter_setting_instagram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_us/', verbose_name='Картинка о нас')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
    ]
