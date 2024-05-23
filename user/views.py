from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from allauth.account.views import (
    PasswordResetView,
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetFromKeyView,
    PasswordResetFromKeyDoneView,
    SignupView,
)


@login_required
def user_profile(request):
    return render(request, "user/profile.html", {"user": request.user})


class CustomPasswordResetView(PasswordResetView):
    template_name = "account/password_reset_form.html"
