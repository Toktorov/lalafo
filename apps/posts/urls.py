from django.urls import path
from apps.posts.views import post_detail


urlpatterns = [
    path('<int:id>', post_detail, name = "post_detail")
]