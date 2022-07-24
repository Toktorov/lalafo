from django.contrib import admin
from apps.users.models import User, UserComment

# Register your models here.
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_user', 'text', 'created')
    
admin.site.register(User)
admin.site.register(UserComment, UserCommentAdmin)