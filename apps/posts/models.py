from distutils.command.upload import upload
from locale import currency
from tabnanny import verbose
from unicodedata import category
from django.db import models
from apps.users.models import User
from apps.categories.models import Category

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_category", blank = True, null = True)
    price = models.PositiveBigIntegerField()
    post_image = models.ImageField(upload_to = "post_image/")
    CHOICE_CURRENCY = (
        ('KGZ', 'KGZ'),
        ('USD', 'USD'),
        ('EURO', 'EURO'),
        ('RUB', 'RUB'),
        ('Договорная', 'Договорная'),
    )
    currency = models.CharField(choices=CHOICE_CURRENCY, default='Договорная', max_length=100)
    phone = models.CharField(max_length=100, default="+99677777777")
    created = models.DateTimeField(auto_now_add=True)
    STATUS_POST = (
        ('Free', 'Free'),
        ('Pro', 'Pro'),
    )
    status = models.CharField(choices=STATUS_POST, max_length=10, default='Free')
    

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="image_post")
    image = models.ImageField(upload_to = "second_post_image/")

    class Meta:
        verbose_name = "Дополнительная фотография"
        verbose_name_plural = "Дополнительные фотографии"