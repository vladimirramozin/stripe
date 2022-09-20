from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='название товара')
    description = models.TextField(verbose_name='описание товара')
    price = models.PositiveIntegerField(verbose_name='цена товара')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

