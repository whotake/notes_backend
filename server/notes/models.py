import uuid

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=180,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id', )


class Note(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=100
    )
    body = models.TextField(
        verbose_name='Содержимое',
        max_length=9999
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_created=True
    )
    category = models.ForeignKey(
        to=Category,
        verbose_name='Категория',
        blank=True,
        null=True
    )
    is_favourite = models.BooleanField(
        verbose_name='В избранном',
        default=False
    )
    uuid = models.UUIDField(
        verbose_name='UUID',
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        to=User,
        verbose_name='Владелец'
    )

    def __str__(self):
        return f'{self.title} - {self.uuid}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ('-id', )
