# home/forms.py

from django import forms
from .models import Subscriber, EmailCampaign

# from ckeditor.widgets import CKEditorWidget


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email", "name"]


class EmailCampaignForm(forms.ModelForm):
    # message = forms.CharField(widget=CKEditorWidget())
    message = forms.Textarea()

    class Meta:
        model = EmailCampaign
        fields = ["subject", "message"]
