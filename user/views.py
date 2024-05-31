from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from allauth.account.views import (
    PasswordResetView,
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetFromKeyView,
    PasswordResetFromKeyDoneView,
    SignupView,
)

from user.models import User


@login_required
def user_profile(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
    return render(request, "user/profile.html", {"profile": profile, 'show_footer': False })


class CustomPasswordResetView(PasswordResetView):
    template_name = "account/password_reset_form.html"
