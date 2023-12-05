from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    telegram = models.CharField(max_length=50, verbose_name='телеграм', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)

    email = models.EmailField(unique=True, verbose_name='почта')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='группа')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
