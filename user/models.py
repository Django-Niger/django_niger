from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass  # Nous n'ajoutons plus de champs directement dans le modèle User


class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ("admin", "Admin"),
        ("moderator", "Moderator"),
        ("member", "Member"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default="member"
    )

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"
