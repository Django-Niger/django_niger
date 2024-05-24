# home/admin.py

from django.contrib import admin
from .models import EmailCampaign, Subscriber
from utils import send_mass_email


class EmailCampaignAdmin(admin.ModelAdmin):
    list_display = ("subject", "created_at")
    actions = ["send_campaign_email"]

    def send_campaign_email(self, request, queryset):
        for campaign in queryset:
            subscribers = Subscriber.objects.all()
            recipient_emails = [subscriber.email for subscriber in subscribers]
            send_mass_email(campaign.subject, campaign.message, recipient_emails)
        self.message_user(request, "Emails sent successfully.")

    send_campaign_email.short_description = "Send selected email campaigns"


admin.site.register(EmailCampaign, EmailCampaignAdmin)
admin.site.register(Subscriber)
