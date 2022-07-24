from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to = "profile_image/", )
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user", verbose_name="От пользователя")
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_for_user", verbose_name="К пользователю")
    rating = models.PositiveBigIntegerField(default=0, verbose_name="Ретинг")
    text = models.TextField(verbose_name="Текст")
    created = models.DateTimeField(auto_now_add=True)
    STATUS_COMMENT = (
        ('В ожидании', 'В ожидании'),
        ('Не принята', 'Не принята'),
        ('Принята', 'Принята'),
    )
    status_comment = models.CharField(choices=STATUS_COMMENT, max_length=30, verbose_name="Статус комментария", default="В ожидании")

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Комментарий пользователю"
        verbose_name_plural = "Комментарии пользователям"