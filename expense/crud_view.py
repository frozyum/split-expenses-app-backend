from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from expense.models import Expense
from expense.serializers import ExpenseSerializer
from group.models import Group


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

