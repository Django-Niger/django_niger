from django.urls import path
from .views import user_profile, test_email

app_name = "user"

urlpatterns = [
    path("profile/", user_profile, name="user_profile"),
    path("test-email/", test_email, name="test_email"),
]
