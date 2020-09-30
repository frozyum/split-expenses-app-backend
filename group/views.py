from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import GroupSerializer
from rest_framework import permissions
from .models import Group


# Create your views here.

class GroupList(ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        new_group = serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Group.objects.all()


class GroupDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Group.objects.filter(owner=self.request.user)
