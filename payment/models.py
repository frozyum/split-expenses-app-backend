from group.models import Group
from django.db import models
from person.models import Person


# Create your models here.


class Payment(models.Model):
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
    froom = models.ForeignKey(to=Person, related_name='from+', on_delete=models.CASCADE)
    too = models.ForeignKey(to=Person, related_name='to', on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField()
    currency = models.CharField(max_length=5)

    def __str__(self):
        return str(self.amount)