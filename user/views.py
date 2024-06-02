from django.shortcuts import render, get_object_or_404, redirect
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

from user.forms import ProfileForm
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
    return render(request, "user/profile.html", {"profile": profile})


@login_required
def profile_update(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user:user_profile')
        form = ProfileForm(instance=request.user.profile)

    return render(request, "user/profile_update.html", {"form": form })


class CustomPasswordResetView(PasswordResetView):
    template_name = "account/password_reset_form.html"
