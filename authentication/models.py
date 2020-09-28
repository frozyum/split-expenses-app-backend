from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    REGULAR = 'RG'
    MANAGER = 'MG'
    ADMIN = 'AD'
    User_Roles = (
        (REGULAR, 'RG'),
        (MANAGER, 'MG'),
        (ADMIN, 'AD'),
    )
    User_Roles = models.CharField(
        max_length=2,
        choices=User_Roles,
        default=REGULAR,
    )




