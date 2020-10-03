from django.urls import path
from .views import GroupExpenseList, ExpenseDetailView

urlpatterns = [
    path('groups/<int:group_id>/expenses', GroupExpenseList.as_view()),
    path('expenses/<int:id>', ExpenseDetailView.as_view()),
]