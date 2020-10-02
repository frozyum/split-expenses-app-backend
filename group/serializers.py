from rest_framework.serializers import ModelSerializer
from .models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'group_photo', 'currency']



