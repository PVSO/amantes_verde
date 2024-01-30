from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    escolhaCargo = (('L', 'Loja'),
                    ('C', 'Cliente'))

    cargo = models.CharField(max_length=1, choices=escolhaCargo)
