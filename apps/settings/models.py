from tabnanny import verbose
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    facebook = models.URLField(null=True)
    twitter = models.URLField(null=True)
    youtube = models.URLField(null=True)
    instagram = models.URLField(null=True)
    linkedin = models.URLField(blank = True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"