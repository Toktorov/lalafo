from distutils.command.upload import upload
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

class AboutUs(models.Model):
    image = models.ImageField(upload_to = 'about_us/', verbose_name="Картинка о нас")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(max_length=100, verbose_name="Почта")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    phone = models.CharField(max_length=100, verbose_name="Телефонный номер")
    problem = models.TextField(verbose_name="Проблема")
    CHOICE_STATUS = (
        ('В ожидании', 'В ожидании'), 
        ('Решена', 'Решена'),
        ('Не решена', 'Не решена'),
    )
    status = models.CharField(choices=CHOICE_STATUS, max_length=30, verbose_name="Статус обращения", default="В ожидании")

    def __str__(self):
        return f"{self.name} {self.title[0:30]}... {self.status}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to = "blog_image/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.description[0:20]}..."

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"

