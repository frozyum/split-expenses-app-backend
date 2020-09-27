from django.http import HttpResponse
from datetime import datetime


def ping_handler(request):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return HttpResponse(dt_string + " (Split Expenses)")
