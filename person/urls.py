from django.urls import path
from .views import GroupPersonList, PersonDetailView

urlpatterns = [
    path('groups/<int:group_id>/persons', GroupPersonList.as_view()),
    path('persons/<int:id>', PersonDetailView.as_view()),
]