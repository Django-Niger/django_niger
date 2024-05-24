from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("subscribe/", views.subscribe, name="subscribe"),
]
