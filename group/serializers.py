from rest_framework.serializers import ModelSerializer
from .models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Group
        fields = ['id', 'name', 'currency']