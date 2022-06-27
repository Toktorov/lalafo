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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    