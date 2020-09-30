from django.db import models
from authentication.models import User


# Create your models here.
class Group(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.TextField()
    group_photo = models.ImageField(upload_to=None, blank=True, null=True)
    currency = models.CharField(max_length=5)

    def __str__(self):
        return str(self.owner) + 's ' + str(self.name)





