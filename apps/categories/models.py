from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Человекопонятный URL (само генерация)")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class ChildenCategory(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_parent")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Человекопонятный URL (само генерация)")


    def __str__(self):
        return f"Категория {self.parent.title}, подкатегория {self.title}"
        
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"