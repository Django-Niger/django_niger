from django.urls import path
from . import views

app_name = "evenement"

urlpatterns = [
    path(
        "events/register/<int:event_id>/",
        views.register_to_event,
        name="register_to_event",
    ),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
]
