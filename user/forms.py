from django import forms
from .models import User


class CustomUserCreationForm(forms.ModelForm):
    # Form for creating new users
    class Meta:
        model = User
        fields = ("username", "email", "user_type", "password")


class CustomUserChangeForm(forms.ModelForm):
    # Form for updating users
    class Meta:
        model = User
        fields = ("username", "email", "user_type")
