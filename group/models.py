from django.db import models
from authentication.models import User


# Create your models here.
class Group(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.TextField()
    currency = models.CharField(max_length=5)

    def __str__(self):
        return str(self.owner) + 's ' + str(self.name)