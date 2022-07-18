from django.urls import path 
from apps.users.views import register, user_login, profile, profile_update, profile_delete, user_favorites

urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', user_login, name = "user_login"),
    path('profile/<int:id>', profile, name = "profile"),
    path('profile/update/<int:id>', profile_update, name = "profile_update"),
    path('profile/delete/<int:id>', profile_delete, name = "profile_delete"),
    path('favorites/user/<int:id>', user_favorites, name = "user_favorites")
]