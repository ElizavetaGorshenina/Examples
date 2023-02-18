from django.db import models
from uuid import uuid4


class User(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    birth_date = models.DateField(null=True)
    email = models.CharField(max_length=256)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
