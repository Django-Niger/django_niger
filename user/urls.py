from django.urls import path
from .views import user_profile

app_name = "user"

urlpatterns = [
    path("profile/", user_profile, name="user_profile"),
]
