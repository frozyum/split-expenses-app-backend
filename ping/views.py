from django.http import HttpResponse
from datetime import datetime

from authentication.decorators import base_auth_required
from utils.datetransformations import default_date_format


@base_auth_required
def ping_handler(request):
    now = datetime.now()
    dt_string = now.strftime(default_date_format)
    return HttpResponse(dt_string + " (Split Expenses)")
