from django.db import models

# Create your models here.
from group.models import Group


class Person(models.Model):
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)

    def __str__(self):
        return str(self.name) + "in " + str(self.group)