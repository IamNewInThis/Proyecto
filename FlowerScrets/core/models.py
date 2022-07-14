from django.db import models
from django.contrib.auth.models import User ## pasar
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save # pasar
from django.dispatch import receiver #pasar


class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut =  models.TextField(max_length=12)
    fechnac = models.DateField()
    numte = models.IntegerField()
    direcc = models.TextField()
    def str(self):
        return self.rut
