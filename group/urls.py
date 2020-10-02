from django.urls import path
from .views import GroupDetailView, GroupList

urlpatterns = [
    path('', GroupList.as_view()),
    path('<int:id>', GroupDetailView.as_view()),
]