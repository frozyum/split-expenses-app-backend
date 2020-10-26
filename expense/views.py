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
    persons_report = {}
    persons = Person.objects.filter(group_id=group_id).all()
    for e in persons:
        persons_report[e.name] = 0

    expenses = Expense.objects.filter(group_id=group_id).all()
    for expense in expenses:
        expense_persons = expense.too.all()
        persons_report[expense.by.name] += expense.amount - (expense.amount / len(expense_persons))
        for expense_person in expense_persons:
            if expense_person.name != expense.by.name:
                persons_report[expense_person.name] -= expense.amount / len(expense_persons)

    payments = Payment.objects.filter(group_id=group_id).all()
    for payment in payments:
        persons_report[payment.froom.name] += payment.amount
        persons_report[payment.too.name] -= payment.amount

    return HttpResponse(json.dumps(persons_report))


@api_view(['GET'])
def get_transaction_list(request, group_id):
    persons_report = {}
    persons = Person.objects.filter(group_id=group_id).all()

    for e in persons:
        persons_report[e.name] = {}
        for j in persons:
            if e.name != j.name:
                persons_report[e.name][j.name] = 0

    expenses = Expense.objects.filter(group_id=group_id).all()

    for expense in expenses:
        expense_persons = expense.too.all()

        for expense_person in expense_persons:
            if expense.by.name != expense_person.name:
                persons_report[expense.by.name][expense_person.name] += expense.amount / len(expense_persons)

    return HttpResponse(json.dumps(persons_report), content_type='application/json')