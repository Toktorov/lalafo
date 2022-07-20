from django.contrib import admin
from apps.settings.models import Setting, AboutUs, Contact, Blog

# Register your models here.
admin.site.register(Setting)
admin.site.register(AboutUs)
admin.site.register(Contact)
admin.site.register(Blog)