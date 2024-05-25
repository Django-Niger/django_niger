# home/middleware.py

from .models import Visitor
from django.utils.deprecation import MiddlewareMixin


class VisitorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip_address = request.META.get("REMOTE_ADDR")
        if (
            not Visitor.objects.filter(ip_address=ip_address).exists()
            and ip_address is not None
        ):
            Visitor.objects.create(ip_address=ip_address)
