from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    class Meta:
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь {self.Login}'

    GENDER_LIST = [
        ('М', 'Мужской'),
        ('Ж', 'Женский')
    ]
    email = models.CharField(max_length=30, verbose_name='Логин пользователя')
    username = models.CharField(max_length=30, verbose_name='Имя пользователя')
    password = models.CharField(max_length=30, verbose_name='Фамилия пользователя')
