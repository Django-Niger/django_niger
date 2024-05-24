from django.core.mail import send_mail
from django.conf import settings


def send_mass_email(subject, message, recipients):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
        fail_silently=False,
    )
