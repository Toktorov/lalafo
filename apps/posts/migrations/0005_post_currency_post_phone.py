# Generated by Django 4.0.5 on 2022-07-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='currency',
            field=models.CharField(choices=[('KGZ', 'KGZ'), ('USD', 'USD'), ('EURO', 'EURO'), ('RUB', 'RUB'), ('Договорная', 'Договорная')], default='Договорная', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default='+99677777777', max_length=100),
        ),
    ]
