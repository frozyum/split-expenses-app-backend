from django.db import models

from authentication.models import User
from group.models import Group
from django.db import models
from person.models import Person


# Create your models here.


class Expense(models.Model):
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
    by = models.ForeignKey(to=Person, related_name='by', on_delete=models.CASCADE)
    too = models.ManyToManyField(to=Person, related_name='expenses')
    title = models.CharField(max_length=24)
    amount = models.FloatField()
    date = models.DateTimeField()
    currency = models.CharField(max_length=5)

    def __str__(self):
        return str(self.title)