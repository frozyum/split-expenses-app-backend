from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from group.models import Group
from .serializers import PersonSerializer
from rest_framework import permissions
from .models import Person


# Create your views here.

class GroupPersonList(ListCreateAPIView):
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "group_id"

    def perform_create(self, serializer, *args, **kwargs):
        new_person = serializer.save(
            group=Group.objects.get(pk=self.kwargs[self.lookup_field]))

    def get_queryset(self):
        return Person.objects.filter(group_id=self.kwargs[self.lookup_field]).all()


class PersonDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Person.objects.filter(id=self.kwargs[self.lookup_field])