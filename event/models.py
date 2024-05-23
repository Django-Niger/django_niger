from django.db import models
from user.models import User


class Category_Evenement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=300)
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)
    category = models.ForeignKey(
        Category_Evenement, on_delete=models.SET_NULL, null=True
    )
    max_participants = models.IntegerField(null=True, blank=True)
    organizers = models.ManyToManyField(User, related_name="organized_events")
    external_link = models.URLField(blank=True, null=True)  # Nouveau champ

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="registrations"
    )
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100
    )  # e.g., 'confirmed', 'waiting', 'cancelled'
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant.user.username} - {self.event.title}"
