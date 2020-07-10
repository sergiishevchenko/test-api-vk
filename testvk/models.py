from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    class Meta:
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь {self.Login}'

    email = models.CharField(max_length=30, verbose_name='Email пользователя')
    username = models.CharField(max_length=30, verbose_name='Имя пользователя')
    password = models.CharField(max_length=30, verbose_name='Пароль пользователя')
