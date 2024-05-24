from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags


def send_mass_email(subject, message, recipients):
    plain_message = strip_tags(message)  # Convert HTML to plain text
    email = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients,
    )
    email.attach_alternative(
        message, "text/html"
    )  # Keep the HTML version as an alternative
    email.send(fail_silently=False)
