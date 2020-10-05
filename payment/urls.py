from django.urls import path
from .views import GroupPaymentList, PaymentDetailView

urlpatterns = [
    path('groups/<int:group_id>/payments', GroupPaymentList.as_view()),
    path('payments/<int:id>', PaymentDetailView.as_view()),
]
