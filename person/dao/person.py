from person.models import Person


def get_persons_by_group_id(group_id):
    persons = Person.objects.filter(group_id=group_id).all()
    return persons


def get_expense_too_persons_list(expense):
    return expense.too.all()

