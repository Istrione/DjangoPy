from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name = 'email', unique = True, blank = True)
    age = models.PositiveIntegerField(null = True, blank = True, verbose_name = 'Возраст')
    avatar = models.ImageField(uploat_to = 'users', blank = True, null = True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
