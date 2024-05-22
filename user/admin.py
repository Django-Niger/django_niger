from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"


class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "user_type")
    search_fields = ("user__username", "user__email", "user_type")


# Enregistrer le modèle User avec l'admin personnalisé
admin.site.register(User, CustomUserAdmin)
# Enregistrer le modèle Profile dans l'administration
admin.site.register(Profile, ProfileAdmin)
