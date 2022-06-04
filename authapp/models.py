from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Возраст')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
