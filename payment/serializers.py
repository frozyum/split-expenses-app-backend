from rest_framework.serializers import ModelSerializer
from .models import Payment


class ExpenseSerializer(ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Payment
        fields = ['id', 'amount', 'date', 'currency', 'froom', 'too']