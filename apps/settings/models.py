from tabnanny import verbose
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название сайта")
    description = models.TextField(verbose_name="Описание сайта")
    logo = models.ImageField(upload_to = 'logo/', verbose_name="Логотип сайта")
    phone = models.CharField(max_length=255, verbose_name="Телефонный номер")
    address = models.CharField(max_length=255, verbose_name="Адрес", blank = True, null = True)
    email = models.EmailField(max_length=150, verbose_name="Электронная почта сайта")
    facebook = models.URLField(blank = True, null=True, verbose_name="Ссылка на facebook")
    twitter = models.URLField(blank = True, null=True, verbose_name="Ссылка на twitter")
    youtube = models.URLField(blank = True, null=True, verbose_name="Ссылка на youtube")
    instagram = models.URLField(blank = True, null=True, verbose_name="Ссылка на instagram")
    linkedin = models.URLField(blank = True, null=True, verbose_name="Ссылка на linkedin")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"