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


class GroupExpenseList(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "group_id"

    def perform_create(self, serializer, *args, **kwargs):
        new_expense = serializer.save(
            group=Group.objects.get(pk=self.kwargs[self.lookup_field]))

    def get_queryset(self):
        return Expense.objects.filter(group_id=self.kwargs[self.lookup_field]).all()


class ExpenseDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Expense.objects.filter(id=self.kwargs[self.lookup_field])


@api_view(['GET'])
def get_report(request, group_id):
    persons_report = get_persons_report(group_id)
    return HttpResponse(json.dumps(persons_report))


@api_view(['GET'])
def get_transaction_list(request, group_id):
    transactions_report = get_transactions_report(group_id)
    return HttpResponse(json.dumps(transactions_report), content_type='application/json')
