from expense.models import Expense


def get_expenses_by_group_id(group_id):
    expenses = Expense.objects.filter(group_id=group_id).all()
    return expenses
