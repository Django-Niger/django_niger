# home/models.py

from django.db import models


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visitor {self.ip_address} on {self.visit_date}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
