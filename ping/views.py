from django.http import HttpResponse
from datetime import datetime

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, authentication_classes

from authentication.decorators import base_auth_required


@base_auth_required
def ping_handler(request):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return HttpResponse(dt_string + " (Split Expenses)")
