from expense.dao.expense import get_expenses_by_group_id
from expense.models import Expense
from payment.dao.payments import get_payments_by_group_id
from payment.models import Payment
from person.dao.person import get_persons_by_group_id, get_expense_too_persons_list
from person.models import Person


def get_transactions_report(group_id):
    persons_report = {}
    persons = get_persons_by_group_id(group_id)

    for e in persons:
        persons_report[e.name] = {}
        for j in persons:
            if e.name != j.name:
                persons_report[e.name][j.name] = 0

    expenses = get_expenses_by_group_id(group_id)

    for expense in expenses:
        expense_persons = get_expense_too_persons_list(expense)

        for expense_person in expense_persons:
            if expense.by.name != expense_person.name:
                persons_report[expense.by.name][expense_person.name] += expense.amount / len(expense_persons)

    return persons_report


def get_persons_report(group_id):
    persons_report = {}
    persons = get_persons_by_group_id(group_id)
    for e in persons:
        persons_report[e.name] = 0

    expenses = get_expenses_by_group_id(group_id)
    for expense in expenses:
        expense_persons = get_expense_too_persons_list(expense)
        persons_report[expense.by.name] += expense.amount - (expense.amount / len(expense_persons))
        for expense_person in expense_persons:
            if expense_person.name != expense.by.name:
                persons_report[expense_person.name] -= expense.amount / len(expense_persons)
    payments = get_payments_by_group_id(group_id)
    for payment in payments:
        persons_report[payment.froom.name] += payment.amount
        persons_report[payment.too.name] -= payment.amount
    return persons_report
