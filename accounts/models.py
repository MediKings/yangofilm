from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(_('email adress'), unique=True)
    phone = models.CharField(_('phone'), max_length=20, unique=True)
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)

    USERNAME_FIELD  = 'email'

    REQUIRED_FIELDS = ['phone']

    objects = CustomUserManager()
