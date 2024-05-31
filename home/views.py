from django.shortcuts import render, redirect
from .models import Visitor, Subscriber
from datetime import datetime
from datetime import datetime
from event.models import Event
from .forms import SubscriberForm
from user.models import User
from django.contrib import messages


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
        "user_count": user_count,
        "form_subscribe": SubscriberForm(),
       "show_footer": True,
    }
    return render(request, "home/landing_page.html", context)


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, "Vous êtes déjà abonné avec cet email.")
        else:
            form = SubscriberForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Vous vous êtes abonné avec succès!")
            else:
                messages.error(
                    request,
                    "L'inscription a échoué. Veuillez vérifier les informations fournies.",
                )
    return redirect("home:landing_page")
