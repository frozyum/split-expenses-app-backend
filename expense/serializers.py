from rest_framework.serializers import ModelSerializer
from .models import Expense


class ExpenseSerializer(ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Expense
        fields = ['id', 'title', 'amount', 'date', 'currency', 'by', 'too']
        extra_kwargs = {'too': {'required': False}}