from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse


@login_required
def user_profile(request):
    return render(request, "user/profile.html", {"user": request.user})


def test_email(request):
    send_mail(
        "Test Email",
        "This is a test email.",
        "django@pythonniger.org",  # Utilisez l'adresse email correcte
        ["hamabarhamou@gmail.com"],  # Remplacez par un email de destinataire valide
        fail_silently=False,
    )
    return HttpResponse("Email sent successfully")
