from django.urls import path 
from apps.settings.views import index, contact, thank_you, blog_detail


urlpatterns = [
    path('', index, name = "index"),
    path('contact/', contact, name = "contact"),
    path('thank_you/', thank_you, name = "thank_you"),
    path('blog/<int:id>', blog_detail, name = "blog_detail"),
]