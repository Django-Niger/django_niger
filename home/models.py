# home/models.py
from django.db import models
from ckeditor.fields import RichTextField


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visitor {self.ip_address} on {self.visit_date}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class EmailCampaign(models.Model):
    subject = models.CharField(max_length=255)
    message = RichTextField()
    # message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
