from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Registration


@login_required
def register_to_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user
    if Registration.objects.filter(event=event, participant=user).exists():
        # Gérer le cas où l'utilisateur est déjà inscrit (par exemple, afficher un message)
        print("Deja inscrit")
        pass
    else:
        Registration.objects.create(event=event, participant=user, status="confirmed")
    return redirect("home:landing_page")


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event/event_detail.html", {"event": event})
