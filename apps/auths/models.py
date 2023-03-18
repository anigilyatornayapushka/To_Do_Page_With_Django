# Django
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
from django.contrib.auth.models import BaseUserManager


class ClientManager(BaseUserManager):
    """Custom user manager."""
    def create_user(self, login: str,
                    password: str) -> 'Client':
        client = Client.objects.create(
            login=login,
            password=password
        )
        client.set_password(password)
        client.save(using=self._db)
        return client
    

    def create_superuser(self, login: str,
                         password: str) -> 'Client':
        client = Client.objects.create(
            login=login,
            password=password
        )
        client.is_staff = True
        client.is_superuser = True
        client.set_password(password)
        client.save(using=self._db)
        return client


class Client(AbstractBaseUser):
    """Custom user model."""
    login: str = models.CharField(
        verbose_name='login',
        max_length=50,
        unique=True,
        null=True
    )
    is_staff: bool = models.BooleanField(
        verbose_name='staff?',
        default=False
    )
    is_superuser: bool = models.BooleanField(
        verbose_name='superuser?',
        default=False
    )
    REQUIRED_FIELDS: list[str] = [
        'password',
    ]
    USERNAME_FIELD: str = 'login'
    objects: ClientManager = ClientManager()

    def __str__(self) -> str:
        return f'{self.id}:{self.login}'
    
    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'user'
        verbose_name_plural = 'users'
