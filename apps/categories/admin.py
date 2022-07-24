from django.contrib import admin
from apps.categories.models import Category, ChildenCategory

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug" : ("title", )}

class ChildenCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title", "parent")}

admin.site.register(Category, CategoryAdmin)
admin.site.register(ChildenCategory, ChildenCategoryAdmin)