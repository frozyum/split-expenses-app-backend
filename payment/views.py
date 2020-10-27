from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from group.models import Group
from .serializers import PaymentSerializer
from rest_framework import permissions
from .models import Payment


# Create your views here.

class GroupPaymentList(ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "group_id"

    def perform_create(self, serializer, *args, **kwargs):
        new_expense = serializer.save(
            group=Group.objects.get(pk=self.kwargs[self.lookup_field]))

    def get_queryset(self):
        return Payment.objects.filter(group_id=self.kwargs[self.lookup_field]).all()


class PaymentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Payment.objects.filter(id=self.kwargs[self.lookup_field])
