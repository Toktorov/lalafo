from django.urls import path
from apps.posts.views import post_detail, post_create, post_update, post_delete, post_search


urlpatterns = [
    path('<int:id>', post_detail, name = "post_detail"),
    path('create/', post_create, name="post_create"),
    path('update/<int:id>', post_update, name = "post_update"),
    path('delete/<int:id>', post_delete, name = "post_delete"),
    path('search/', post_search, name = "post_search"),
]