from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(verbose_name=_('email'), unique=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('age'))
    avatar = models.ImageField(upload_to='users', blank=True, null=True, verbose_name=_('avatar'))

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
