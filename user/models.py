from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ("admin", "Admin"),
        ("moderator", "Moderator"),
        ("member", "Member"),
    )
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default="member"
    )
