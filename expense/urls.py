from django.urls import path
from .views import GroupExpenseList, ExpenseDetailView
from . import views

urlpatterns = [
    path('groups/<int:group_id>/expenses', GroupExpenseList.as_view()),
    path('expenses/<int:id>', ExpenseDetailView.as_view()),
    path('groups/<int:group_id>/report', views.get_report),
    path('groups/<int:group_id>/get_transaction_list', views.get_transaction_list),

]