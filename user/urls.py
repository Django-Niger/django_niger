from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("profile/", views.user_profile, name="user_profile"),
    path("profile/edit/", views.profile_update, name="profile_update"),
    path("accounts/password/reset/", views.CustomPasswordResetView.as_view(), name="account_reset_password",),
]
