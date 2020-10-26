from expense.dao.expense import get_expenses_by_group_id
from person.dao.person import get_persons_by_group_id, get_expense_too_persons_list


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


