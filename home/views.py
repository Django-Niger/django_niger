from django.shortcuts import render, redirect
from .models import Visitor, Subscriber
from datetime import datetime
from datetime import datetime
from event.models import Event
from .forms import SubscriberForm
from user.models import User


# Create your views here.
def landing_page(request):
    upcoming_events = Event.objects.filter(date_time__gt=datetime.now()).order_by(
        "date_time"
    )
    visitor_count = Visitor.objects.count()
    subscriber_count = Subscriber.objects.count()
    user_count = User.objects.count()  # Ajout du comptage des utilisateurs inscrits

    context = {
        "upcoming_events": upcoming_events,
        "visitor_count": visitor_count,
        "subscriber_count": subscriber_count,
        "user_count": user_count,  # Ajout du nombre d'utilisateurs inscrits au contexte
    }
    return render(request, "home/landing_page.html", context)


def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:landing_page")
    return redirect("home:landing_page")
