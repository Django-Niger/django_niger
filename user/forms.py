from .models import *

from django import forms
from .models import User


class CustomUserCreationForm(forms.ModelForm):
    # Form for creating new users
    class Meta:
        model = User
        fields = ("username", "email",  "password")


class CustomUserChangeForm(forms.ModelForm):
    # Form for updating users
    class Meta:
        model = User
        fields = ("username", "email",)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'user_type']

        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows': 3})
        }
