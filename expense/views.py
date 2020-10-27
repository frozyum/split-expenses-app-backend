import json
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .services.reportservice import get_transactions_report, get_persons_report


# Create your views here.

@api_view(['GET'])
def get_report(request, group_id):
    persons_report = get_persons_report(group_id)
    return HttpResponse(json.dumps(persons_report))


@api_view(['GET'])
def get_transaction_list(request, group_id):
    transactions_report = get_transactions_report(group_id)
    return HttpResponse(json.dumps(transactions_report), content_type='application/json')