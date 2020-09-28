from django.http import HttpResponse
from datetime import datetime

from utils.datetransformations import default_date_format


def ping_handler(request):
    now = datetime.now()
    dt_string = now.strftime(default_date_format)
    return HttpResponse(dt_string + " (Split Expenses) Davitich")
