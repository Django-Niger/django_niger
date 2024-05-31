from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class User(AbstractUser):
    pass  # Nous n'ajoutons plus de champs directement dans le modèle User


class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ("admin", "Admin"),
        ("moderator", "Moderator"),
        ("member", "Member"),
    )
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="member")
    bio = models.TextField(null=True, blank=True)

    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar_default.svg')
        return avatar

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"
