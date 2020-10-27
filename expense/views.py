import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from authentication.models import User
from group.models import Group
from .serializers import ExpenseSerializer
from rest_framework import permissions
from .models import Expense
from person.models import Person
from payment.models import Payment

# Create your views here.
from .services.reportservice import get_transactions_report, get_persons_report


@api_view(['GET'])
def get_report(request, group_id):
    persons_report = get_persons_report(group_id)
    return HttpResponse(json.dumps(persons_report))


@api_view(['GET'])
def get_transaction_list(request, group_id):
    transactions_report = get_transactions_report(group_id)
    return HttpResponse(json.dumps(transactions_report), content_type='application/json')
