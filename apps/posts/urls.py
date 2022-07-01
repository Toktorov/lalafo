from django.urls import path
from apps.posts.views import post_detail, post_create


urlpatterns = [
    path('<int:id>', post_detail, name = "post_detail"),
    path('create/', post_create, name="post_create"),
]