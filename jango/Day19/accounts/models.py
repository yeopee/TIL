from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    address = models.CharField(max_length=200)
    fans = models.ManyToManyField('self', related_name='stars')
