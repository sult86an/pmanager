from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Leaders(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname
