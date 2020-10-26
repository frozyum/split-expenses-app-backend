from payment.models import Payment


def get_payments_by_group_id(group_id):
    payments = Payment.objects.filter(group_id=group_id).all()
    return payments
