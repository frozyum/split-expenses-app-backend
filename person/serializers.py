from rest_framework.serializers import ModelSerializer
from expense.serializers import ExpenseSerializer
from .models import Person


class PersonSerializer(ModelSerializer):
    expenses = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Person
        fields = ['id', 'name', 'expenses']
        extra_kwargs = {'persons': {'required': False}}