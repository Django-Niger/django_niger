# home/forms.py

from django import forms
from .models import Subscriber, EmailCampaign


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email", "name"]


class EmailCampaignForm(forms.ModelForm):
    class Meta:
        model = EmailCampaign
        fields = ["subject", "message"]
